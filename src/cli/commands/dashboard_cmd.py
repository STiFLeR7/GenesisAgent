from src.analytics.dashboard import print_dashboard
from src.storage.persistence import fetch_top

def run(limit=10):
    data = [{"idea": c, "score": s} for c, s in fetch_top(limit)]
    print_dashboard(data)
