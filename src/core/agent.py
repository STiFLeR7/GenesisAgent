import random
from src.core.evolution import EvolutionEngine

class AgentMemory:
    """Stores all ideas across generations"""
    def __init__(self):
        self.history = []

    def add(self, generation, ideas):
        self.history.append({"gen": generation, "ideas": ideas})

    def get_all(self):
        return self.history


class SelfEvaluator:
    """Scores ideas based on simple heuristics"""
    @staticmethod
    def score(idea: str) -> float:
        # Very simple scoring: reward diversity + length (placeholder for now)
        unique_words = len(set(idea.split()))
        length_factor = len(idea.split())
        return unique_words * 0.6 + length_factor * 0.4


class GenesisAgent:
    """Autonomous evolutionary creativity agent"""
    def __init__(self, n=5, max_generations=5, goal=None):
        self.engine = EvolutionEngine()
        self.memory = AgentMemory()
        self.evaluator = SelfEvaluator()
        self.n = n
        self.max_generations = max_generations
        self.goal = goal if goal else "creative exploration"

    def run(self):
        pool = self.engine.generator.generate(self.n)
        self.memory.add(0, pool)

        for gen in range(1, self.max_generations + 1):
            mutated = [self.engine.mutate(idea) for idea in pool]
            scored = [(idea, self.evaluator.score(idea)) for idea in mutated]
            # Select top-n by score
            scored.sort(key=lambda x: x[1], reverse=True)
            pool = [idea for idea, _ in scored[:self.n]]
            self.memory.add(gen, pool)

            # Simple stop condition: if avg score above threshold
            avg_score = sum(score for _, score in scored) / len(scored)
            if avg_score > 25:  # arbitrary threshold for now
                break

        return self.memory.get_all()
