from src.core.generator import IdeaGenerator

def test_generate():
    gen = IdeaGenerator()
    ideas = gen.generate(2)
    assert len(ideas) == 2
    assert isinstance(ideas[0], str)
