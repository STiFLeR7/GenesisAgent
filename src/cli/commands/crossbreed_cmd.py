from src.core.population_manager import Population
from src.utils.logger import log

def run(idea_a, idea_b):
    pop = Population()
    child = pop.crossbreed(idea_a, idea_b)
    log(f"Crossbred idea: {child}")
