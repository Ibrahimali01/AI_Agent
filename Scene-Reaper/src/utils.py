import yaml
from pathlib import Path

def load_config(config_path=None):
    if config_path is None:
        config_path = Path(__file__).parent.parent / "config" / "config.yaml"
    config_path = Path(config_path)
    if not config_path.exists():
        return {}
    with open(config_path, 'r') as f:
        return yaml.safe_load(f) or {}
