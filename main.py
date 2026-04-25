
import json
import os

os.makedirs("data", exist_ok=True)

data = {
    "name": "brain",
    "version": 1.0,
    "content": "This is brain data."
}

with open("data/brain.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
