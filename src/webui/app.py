"""
GenesisAgent v2.0.0 — Localhost Chat Server
Run with:
    uvicorn src.webui.app:app --reload --port 8000
"""

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from pathlib import Path

from src.storage.persistence import init_db, fetch_top, store_idea
from src.core.population_manager import Population

# ---------------------------------------------------------------------
# Paths & Initialization
# ---------------------------------------------------------------------
BASE_DIR = Path(__file__).resolve().parent
STATIC_DIR = BASE_DIR / "static"
INDEX_FILE = STATIC_DIR / "index.html"

# Initialize DB + population
init_db()
population = Population(n_agents=3, crossbreed_rate=0.4)

# FastAPI instance
app = FastAPI(title="GenesisAgent v2.0.0 — Localhost Chat")

# CORS middleware (for JS access)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve static files under /static
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")

# ---------------------------------------------------------------------
# In-memory conversation state
# ---------------------------------------------------------------------
conversation_history: list[dict] = []

# ---------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------

@app.get("/", response_class=FileResponse)
async def serve_home():
    """Serve the main React frontend."""
    return FileResponse(INDEX_FILE)


@app.post("/chat")
async def chat_post(request: Request):
    """
    Run GenesisAgent evolution loop for the user prompt (POST JSON).
    Body: {"prompt": "your prompt"}
    Returns: {"prompt_sent": "...", "reply": "...", "conversation_count": N}
    """
    try:
        body = await request.json()
    except Exception:
        body = {}
    prompt = body.get("prompt", "") if isinstance(body, dict) else ""
    if not isinstance(prompt, str):
        prompt = str(prompt)

    # Run evolution and pick best
    records = population.evolve_all(generations=2)
    if not records:
        reply = "No ideas generated."
        best = {"idea": "", "score": 0.0, "agent_id": -1, "generation": -1}
    else:
        best = max(records, key=lambda x: x.get("score", 0.0))
        reply = (
            f"Prompt: {prompt}\n\n"
            f"GenesisAgent proposes:\n"
            f"→ {best.get('idea','')} (score {best.get('score',0.0):.3f})"
        )

    # Persist best idea (if present)
    try:
        store_idea(best.get("idea", ""), best.get("score", 0.0),
                   best.get("agent_id", -1), best.get("generation", -1))
    except Exception:
        # persistence failure shouldn't break response
        pass

    # Update conversation memory
    conversation_history.append({"prompt": prompt, "reply": reply})

    return JSONResponse({
        "prompt_sent": prompt,
        "reply": reply,
        "conversation_count": len(conversation_history)
    })


@app.get("/api/top")
async def get_top(limit: int = 6):
    """Retrieve top evolved ideas from SQLite."""
    try:
        data = fetch_top(limit)
    except Exception:
        data = []
    return {"ideas": [{"content": c, "score": s} for c, s in data]}


@app.get("/api/history")
async def get_history():
    """Return recent conversation memory (last 10)."""
    return {"history": conversation_history[-10:]}


@app.get("/api/clear-history")
async def clear_history():
    """Reset in-memory chat history."""
    conversation_history.clear()
    return {"status": "cleared", "remaining": len(conversation_history)}


@app.get("/health")
async def health_check():
    return {"status": "ok", "msg": "GenesisAgent is running"}
