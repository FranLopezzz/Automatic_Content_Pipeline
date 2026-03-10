import json
import os
from pathlib import Path
from datetime import datetime

OUTPUT_DIR = Path(__file__).parent.parent.parent / "output"


def get_state_path(run_id):
    return OUTPUT_DIR / run_id / "state.json"


def read_state(run_id):
    """Read run state from JSON file."""
    state_path = get_state_path(run_id)
    if not state_path.exists():
        return None
    with open(state_path, "r", encoding="utf-8") as f:
        return json.load(f)


def write_state(run_id, state):
    """Write run state to JSON file atomically."""
    state_path = get_state_path(run_id)
    state_path.parent.mkdir(parents=True, exist_ok=True)
    state["updated_at"] = datetime.utcnow().isoformat() + "Z"
    tmp_path = str(state_path) + ".tmp"
    with open(tmp_path, "w", encoding="utf-8") as f:
        json.dump(state, f, indent=2, ensure_ascii=False)
    os.replace(tmp_path, str(state_path))
    return state


def update_stage(run_id, new_stage, extra_data=None):
    """Update the stage of a run and optionally merge extra data."""
    state = read_state(run_id)
    if not state:
        raise ValueError(f"Run {run_id} not found")
    state["stage"] = new_stage
    if extra_data:
        state.update(extra_data)
    return write_state(run_id, state)
