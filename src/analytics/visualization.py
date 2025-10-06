"""
Generates basic ASCII heatmaps or graphs (stubbed for CLI view).
"""

def render_heatmap(values: list[float], label: str = "Heatmap"):
    bars = "".join(["█" if v > 0.5 else "░" for v in values])
    print(f"{label}: {bars}")
