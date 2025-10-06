"""
CLI command to generate themed ideas.
"""

from src.core.generator import generate_idea
from src.utils.logger import log

def run(theme: str = None):
    idea = generate_idea(theme)
    log(f"Generated idea: {idea}")
