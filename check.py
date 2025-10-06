from src.storage.persistence import init_db
from src.core.population_manager import Population
from src.analytics.dashboard import print_dashboard

init_db()
p = Population(n_agents=3, crossbreed_rate=0.5)
records = p.evolve_all(generations=3)
print_dashboard(records)