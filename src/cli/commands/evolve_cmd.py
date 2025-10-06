from src.core.population import Population
from src.utils.logger import log

def run(n_agents: int = 3, generations: int = 3):
    pop = Population(n_agents)
    results = pop.evolve_all(generations)
    log(f"Evolved {len(results)} ideas using {n_agents} agents.")
