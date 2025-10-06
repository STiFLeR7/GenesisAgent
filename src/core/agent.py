"""
GenesisAgent v2.0.0 — Autonomous Cognitive Agent
Each agent evolves ideas using generation, mutation, and symbolic cognition.
"""

from src.core.generator import generate_idea
from src.core.mutator import mutate_idea
from src.cognition.symbolic_engine import recombine_ideas, infer_context
from src.scorer import score_idea
from src.utils.logger import log


class Agent:
    """An autonomous unit with symbolic cognition."""

    def __init__(self, agent_id: int, config: dict | None = None):
        self.agent_id = agent_id
        self.config = config or {}
        self.pool = []

    def evolve(self, generations: int = 3) -> list[dict]:
        """Run full cognitive evolution: generation → mutation → recombination."""
        log(f"[Agent-{self.agent_id}] Evolution start ({generations} generations)")
        last_idea = None

        for gen in range(generations):
            idea = generate_idea(self.config.get("theme"))
            mutated = mutate_idea(idea)
            ctx = infer_context(mutated)
            hybrid = recombine_ideas(mutated, last_idea) if last_idea else mutated
            last_idea = hybrid
            fitness = score_idea(hybrid)
            record = {
                "idea": hybrid,
                "score": fitness,
                "context": ctx,
                "generation": gen,
                "agent_id": self.agent_id,
            }
            self.pool.append(record)
            log(f"[Agent-{self.agent_id}] Gen {gen+1}: Score={fitness:.3f}, Keywords={ctx['keywords'][:3]}")
        return self.pool
