"""
GenesisAgent v2.0.0 — Multi-Agent Cognitive Population Manager
Handles cooperative evolution, symbolic crossbreeding, and persistence.
"""

import random
from src.core.agent import Agent
from src.cognition.symbolic_engine import recombine_ideas
from src.storage.persistence import store_idea
from src.utils.logger import log


class Population:
    """Manages multiple cognitive agents and symbolic crossbreeding."""

    def __init__(self, n_agents: int = 3, crossbreed_rate: float = 0.3):
        self.agents = [Agent(i) for i in range(n_agents)]
        self.crossbreed_rate = crossbreed_rate

    def evolve_all(self, generations: int = 3) -> list[dict]:
        """Run evolution across all agents with persistence."""
        all_records = []

        for gen in range(generations):
            log(f"\n=== Generation {gen+1}/{generations} ===")
            gen_records = []

            for agent in self.agents:
                evolved = agent.evolve(1)
                for r in evolved:
                    store_idea(r["idea"], r["score"], r["agent_id"], r["generation"])
                gen_records.extend(evolved)

            if len(gen_records) >= 2 and random.random() < self.crossbreed_rate:
                a, b = random.sample(gen_records, 2)
                hybrid = recombine_ideas(a["idea"], b["idea"])
                log(f"[Crossbreed] Agent-{a['agent_id']} × Agent-{b['agent_id']} → Hybrid")
                hybrid_record = {
                    "idea": hybrid,
                    "score": random.uniform(0.4, 0.9),
                    "generation": gen,
                    "agent_id": -1,
                    "context": {"keywords": ["hybrid", "symbolic"], "length": len(hybrid.split())},
                }
                store_idea(hybrid_record["idea"], hybrid_record["score"],
                           hybrid_record["agent_id"], hybrid_record["generation"])
                gen_records.append(hybrid_record)

            all_records.extend(gen_records)

        log(f"\n[Population] Evolution complete. Total records: {len(all_records)}")
        return all_records

    def crossbreed(self, idea_a: str, idea_b: str) -> str:
        hybrid = recombine_ideas(idea_a, idea_b)
        log(f"[Manual Crossbreed] → {hybrid[:60]}…")
        return hybrid
