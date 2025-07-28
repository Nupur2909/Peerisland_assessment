import json
import src.config

def write_summaries_to_json(summaries):
    try:
        with open(config.OUTPUT_PATH, "w") as f:
            json.dump(summaries, f, indent=2)
        print(f"✅ Output written to {config.OUTPUT_PATH}")
    except Exception as e:
        print(f"❌ Error writing output: {e}")