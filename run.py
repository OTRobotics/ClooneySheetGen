import json
import sys
from sheet import Sheet


if __name__ == "__main__":
    config = json.load(open("resources/powerup_config.json", "r", encoding="utf-8"))
    if len(sys.argv) >= 2:
        # Format: <event-name> [event-id] [frc-api-token]
        config['event'] = sys.argv[1]
        if len(sys.argv) >= 3:
            config['event_code'] = sys.argv[2]
            if len(sys.argv) >= 4:
                config['frc_api'] = sys.argv[3]

    print("Generating scouting sheets for " + config['event_code'] + " - " + config['event'])
    gen = Sheet(config)
    fields = json.load(open("resources/powerup_test_3.json", "r", encoding="utf-8"))
    gen.create_from_json(fields)
    
def test_sheetGeneration():
    config = json.load(open("resources/powerup_config.json", "r", encoding="utf-8"))
    gen = Sheet(config)
    fields = json.load(open("resources/powerup_test_3.json", "r", encoding="utf-8"))
    gen.create_from_json(fields)
    pass
