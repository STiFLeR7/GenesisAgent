# src/core/evolution.py
import random
from .generator import IdeaGenerator
from .mutator import Mutator
from .polisher import heuristic_scores

class EvolutionEngine:
    def __init__(self, seed=None):
        self.rng = random.Random(seed)
        self.generator = IdeaGenerator(seed=seed)
        self.mutator = Mutator(seed=seed)

    def _make_obj(self, base):
        return {"base": base, "twists": []}

    def _recombine(self, a, b, max_twists):
        """
        Hybridize two ideas: choose one base; mix a subset of unique twists.
        """
        base = self.rng.choice([a["base"], b["base"]])
        pool = list(set(a["twists"] + b["twists"]))  # dedup identical (cat, phrase)
        self.rng.shuffle(pool)
        take = self.rng.randint(1, min(3, len(pool))) if pool else 0
        child = {"base": base, "twists": pool[:take]}
        return self.mutator.prune(child, max_twists=max_twists)

    def _score(self, idea_obj):
        """
        Heuristic novelty/clarity/feasibility scores based on spread & size.
        """
        return heuristic_scores(idea_obj)

    def evolve(self, n=5, generations=3, max_twists=6, recombination_chance=0.2):
        """
        Returns a list of generations; each generation is a list of formatted idea strings.
        """
        # Gen 0 population
        bases = self.generator.generate(n)
        population = [self._make_obj(b) for b in bases]

        history_strings = []
        # Generation 0 (plain bases)
        gen0 = [self.mutator.format(obj) for obj in population]
        history_strings.append(gen0)

        for _g in range(1, generations + 1):
            # Mutate each idea 1-2 twists, then prune
            new_population = []
            for obj in population:
                obj = {"base": obj["base"], "twists": list(obj["twists"])}
                obj = self.mutator.mutate(obj, add_min=1, add_max=2)
                obj = self.mutator.prune(obj, max_twists=max_twists)
                new_population.append(obj)

            # Recombination (optional)
            if self.rng.random() < float(recombination_chance) and len(new_population) >= 2:
                parents = self.rng.sample(new_population, 2)
                child = self._recombine(parents[0], parents[1], max_twists=max_twists)
                # Replace the weakest (fewest category variety) with child
                def variety(o): return len(set(c for c, _ in o["twists"]))
                weakest_idx = min(range(len(new_population)), key=lambda i: variety(new_population[i]))
                new_population[weakest_idx] = child

            # Small dedupe across the generation (base + phrase set)
            seen_keys = set()
            deduped = []
            for obj in new_population:
                key = (obj["base"], tuple(p for (_, p) in obj["twists"]))
                if key in seen_keys:
                    continue
                seen_keys.add(key)
                deduped.append(obj)

            # Pad if dedup shrank
            while len(deduped) < n:
                base = self.generator.generate(1)[0]
                deduped.append(self._make_obj(base))

            # Score & format
            formatted = []
            for obj in deduped[:n]:
                n_score, c_score, f_score = self._score(obj)
                formatted.append(self.mutator.format(obj, (n_score, c_score, f_score)))

            history_strings.append(formatted)
            population = deduped[:n]

        return history_strings
