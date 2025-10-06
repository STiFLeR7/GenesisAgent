"""
GenesisAgent v2.0.0 Chat API — powered by FastAPI + Uvicorn
Run with:  uvicorn src.webui.app:app --reload --port 8000
"""

from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
from src.storage.persistence import init_db, fetch_top
from src.core.population_manager import Population
from src.analytics.dashboard import print_dashboard

# Initialize DB and app
init_db()
app = FastAPI(title="GenesisAgent v2.0.0 Chat API")
population = Population(n_agents=3, crossbreed_rate=0.4)


@app.get("/")
async def home():
    """Simple HTML interface."""
    html = """
    <html>
      <head><title>GenesisAgent Chat</title></head>
      <body style="background-color:#111;color:#fff;font-family:monospace;">
        <h2>GenesisAgent v2.0.0 — Cognitive Chatbot</h2>
        <form id="form">
            <input type="text" id="prompt" style="width:70%;" placeholder="Ask GenesisAgent..." autofocus />
            <button>Send</button>
        </form>
        <pre id="response"></pre>
        <script>
          const form = document.getElementById("form");
          form.addEventListener("submit", async (e)=>{
              e.preventDefault();
              const input = document.getElementById("prompt").value;
              const res = await fetch('/chat?prompt=' + encodeURIComponent(input));
              const data = await res.json();
              document.getElementById("response").innerText = data.reply;
          });
        </script>
      </body>
    </html>
    """
    return HTMLResponse(html)


@app.get("/chat")
async def chat(prompt: str):
    """
    Generate evolved ideas based on user prompt.
    Uses symbolic cognition + population-level evolution.
    """
    records = population.evolve_all(generations=2)
    # Pick the highest scoring idea and return it
    best = sorted(records, key=lambda x: x["score"], reverse=True)[0]
    reply = (
        f"Prompt: {prompt}\n\n"
        f"GenesisAgent proposes:\n"
        f"→ {best['idea']} (score {best['score']})"
    )
    return {"reply": reply}


@app.get("/top")
async def get_top(limit: int = 5):
    """Retrieve top ideas from SQLite."""
    data = fetch_top(limit)
    return {"ideas": [{"content": c, "score": s} for c, s in data]}


@app.get("/dashboard")
async def dashboard():
    """Return a quick CLI-like dashboard view."""
    records = population.evolve_all(generations=1)
    print_dashboard(records)
    return {"status": "ok", "message": "Dashboard printed to console"}
"""
GenesisAgent v2.0.0 Chat API — powered by FastAPI + Uvicorn
Run with:  uvicorn src.webui.app:app --reload --port 8000
"""

from fastapi import FastAPI, WebSocket, Request
from fastapi.responses import HTMLResponse
from src.storage.persistence import init_db, fetch_top
from src.core.population_manager import Population
from src.analytics.dashboard import print_dashboard

# Initialize DB and app
init_db()
app = FastAPI(title="GenesisAgent v2.0.0 Chat API")
population = Population(n_agents=3, crossbreed_rate=0.4)


@app.get("/")
async def home():
    """Simple HTML interface."""
    html = """
    <html>
      <head><title>GenesisAgent Chat</title></head>
      <body style="background-color:#111;color:#fff;font-family:monospace;">
        <h2>GenesisAgent v2.0.0 — Cognitive Chatbot</h2>
        <form id="form">
            <input type="text" id="prompt" style="width:70%;" placeholder="Ask GenesisAgent..." autofocus />
            <button>Send</button>
        </form>
        <pre id="response"></pre>
        <script>
          const form = document.getElementById("form");
          form.addEventListener("submit", async (e)=>{
              e.preventDefault();
              const input = document.getElementById("prompt").value;
              const res = await fetch('/chat?prompt=' + encodeURIComponent(input));
              const data = await res.json();
              document.getElementById("response").innerText = data.reply;
          });
        </script>
      </body>
    </html>
    """
    return HTMLResponse(html)


@app.get("/chat")
async def chat(prompt: str):
    """
    Generate evolved ideas based on user prompt.
    Uses symbolic cognition + population-level evolution.
    """
    records = population.evolve_all(generations=2)
    # Pick the highest scoring idea and return it
    best = sorted(records, key=lambda x: x["score"], reverse=True)[0]
    reply = (
        f"Prompt: {prompt}\n\n"
        f"GenesisAgent proposes:\n"
        f"→ {best['idea']} (score {best['score']})"
    )
    return {"reply": reply}


@app.get("/top")
async def get_top(limit: int = 5):
    """Retrieve top ideas from SQLite."""
    data = fetch_top(limit)
    return {"ideas": [{"content": c, "score": s} for c, s in data]}


@app.get("/dashboard")
async def dashboard():
    """Return a quick CLI-like dashboard view."""
    records = population.evolve_all(generations=1)
    print_dashboard(records)
    return {"status": "ok", "message": "Dashboard printed to console"}
