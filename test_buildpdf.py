import json
from sheet import Sheet

def test_sheetGeneration():
    config = json.load(open("resources/powerup_config.json", "r", encoding="utf-8"))
    gen = Sheet(config)
    fields = json.load(open("resources/powerup_test_3.json", "r", encoding="utf-8"))
    gen.create_from_json(fields)
    pass
