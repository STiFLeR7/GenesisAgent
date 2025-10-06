"""
Simple colorless logger (streamlined for cross-platform).
"""

from datetime import datetime

def log(msg: str, level: str = "INFO"):
    now = datetime.now().strftime("%H:%M:%S")
    print(f"[{now}] [{level}] {msg}")
