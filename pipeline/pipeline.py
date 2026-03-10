"""Franlopezaz UGC Engine — Pipeline Orchestrator

Usage:
    python pipeline.py --run-id 20260310_143022 --advance-one
    python pipeline.py --run-id 20260310_143022 --stage brief
    python pipeline.py --worker
    python pipeline.py --scheduled
"""

import argparse
import json
import time
import sys
from pathlib import Path
from datetime import datetime

# Ensure imports work
sys.path.insert(0, str(Path(__file__).parent))

from lib.run_state import read_state, write_state, OUTPUT_DIR
from stages import STAGE_MAP


def advance_one(run_id):
    """Advance a run by one stage."""
    state = read_state(run_id)
    if not state:
        print(f"[pipeline] Run {run_id} not found")
        return False

    current_stage = state["stage"]
    if current_stage not in STAGE_MAP:
        print(f"[pipeline] Cannot advance from stage '{current_stage}'")
        return False

    next_stage, execute_fn = STAGE_MAP[current_stage]
    output_dir = OUTPUT_DIR / run_id

    print(f"[pipeline] {run_id}: {current_stage} → {next_stage}")

    try:
        state = execute_fn(state, output_dir)
        write_state(run_id, state)
        print(f"[pipeline] {run_id}: Stage '{next_stage}' completed")
        return True
    except Exception as e:
        state["status"] = "error"
        state["error"] = str(e)
        write_state(run_id, state)
        print(f"[pipeline] {run_id}: Error in stage '{next_stage}': {e}")
        return False


def run_stage(run_id, stage_name):
    """Run a specific stage for a run."""
    state = read_state(run_id)
    if not state:
        print(f"[pipeline] Run {run_id} not found")
        return False

    # Find the stage function
    for src_stage, (target_stage, execute_fn) in STAGE_MAP.items():
        if target_stage == stage_name:
            output_dir = OUTPUT_DIR / run_id
            print(f"[pipeline] {run_id}: Running stage '{stage_name}'")
            try:
                state = execute_fn(state, output_dir)
                write_state(run_id, state)
                print(f"[pipeline] {run_id}: Stage '{stage_name}' completed")
                return True
            except Exception as e:
                state["status"] = "error"
                state["error"] = str(e)
                write_state(run_id, state)
                print(f"[pipeline] {run_id}: Error in stage '{stage_name}': {e}")
                return False

    print(f"[pipeline] Unknown stage: {stage_name}")
    return False


def worker_loop():
    """Process pending runs from queue continuously."""
    queue_path = Path(__file__).parent.parent / "api" / "data" / "queue.json"
    print("[pipeline] Worker mode started. Watching queue...")

    while True:
        try:
            if queue_path.exists():
                with open(queue_path, "r", encoding="utf-8") as f:
                    queue = json.load(f)

                for entry in queue:
                    run_id = entry["id"]
                    state = read_state(run_id)
                    if state and state["stage"] != "published" and state.get("status") != "error":
                        advance_one(run_id)
        except Exception as e:
            print(f"[pipeline] Worker error: {e}")

        time.sleep(30)


def main():
    parser = argparse.ArgumentParser(description="Franlopezaz UGC Engine Pipeline")
    parser.add_argument("--run-id", help="Run ID to process")
    parser.add_argument("--stage", help="Specific stage to execute")
    parser.add_argument("--advance-one", action="store_true", help="Advance run by one stage")
    parser.add_argument("--worker", action="store_true", help="Run as queue worker")
    parser.add_argument("--scheduled", action="store_true", help="Run with APScheduler")

    args = parser.parse_args()

    if args.worker:
        worker_loop()
    elif args.scheduled:
        from lib.scheduler import create_scheduler
        scheduler = create_scheduler(lambda: None)  # TODO: wire callback
        scheduler.start()
        print("[pipeline] Scheduled mode. Press Ctrl+C to exit.")
        try:
            while True:
                time.sleep(60)
        except KeyboardInterrupt:
            scheduler.shutdown()
    elif args.run_id:
        if args.advance_one:
            advance_one(args.run_id)
        elif args.stage:
            run_stage(args.run_id, args.stage)
        else:
            print("[pipeline] Specify --advance-one or --stage <name>")
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
