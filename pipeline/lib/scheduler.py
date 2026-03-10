"""APScheduler configuration for autonomous pipeline execution."""

import json
from pathlib import Path
from apscheduler.schedulers.background import BackgroundScheduler


CONFIG_PATH = Path(__file__).parent.parent.parent / "api" / "data" / "config.json"


def load_schedule_config():
    """Load schedule configuration from config.json."""
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        config = json.load(f)
    return config.get("pipeline", {}).get("schedule", {})


def create_scheduler(run_callback):
    """Create and configure APScheduler.

    Args:
        run_callback: Function to call on each scheduled tick.
                      Should process the next pending run in the queue.
    """
    scheduler = BackgroundScheduler()
    config = load_schedule_config()

    if not config.get("enabled", False):
        print("[scheduler] Scheduled execution is disabled in config")
        return scheduler

    hours = config.get("hours", [9, 12, 15, 18])
    for hour in hours:
        scheduler.add_job(
            run_callback,
            "cron",
            hour=hour,
            minute=0,
            id=f"morfeo_run_{hour}",
            replace_existing=True
        )
        print(f"[scheduler] Scheduled run at {hour}:00")

    return scheduler
