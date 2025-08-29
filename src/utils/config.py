import yaml
from pathlib import Path

def load_config(path="config.yaml"):
    if Path(path).exists():
        with open(path, "r") as f:
            return yaml.safe_load(f)
    return {}
