"""
Optional local LLM interface (Ollama, llama.cpp, etc.).
Fallbacks to deterministic symbolic reasoning if no model is loaded.
"""

import os

def generate_with_llm(prompt: str) -> str:
    if os.getenv("GENESIS_USE_LLM") != "1":
        return f"[LLM disabled] {prompt}"
    # Placeholder for local inference (to be integrated later)
    return f"[LLM simulated response] {prompt}"
