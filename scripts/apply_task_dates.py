#!/usr/bin/env python3
"""
Apply start and due dates to all tasks in the Asana project using relative date anchoring.

Formula:
- Start Date = Launch Date - Days Before Launch
- Due Date = Start Date + Duration - 1
"""

import json
from datetime import datetime, timedelta
from pathlib import Path

# File paths
SCRIPT_DIR = Path(__file__).parent
PROJECT_ROOT = SCRIPT_DIR.parent
TASK_GID_MAPPING = PROJECT_ROOT / "task_gid_mapping.json"
TASK_DATES_MAPPING = PROJECT_ROOT / "task_dates_mapping.json"

def load_json(filepath):
    """Load JSON file."""
    with open(filepath, 'r') as f:
        return json.load(f)

def calculate_dates(launch_date_str, days_before_launch, duration_days):
    """Calculate start and due dates based on launch date anchor.

    Args:
        launch_date_str: Launch date in YYYY-MM-DD format
        days_before_launch: Days before launch this task starts
        duration_days: Task duration in days

    Returns:
        tuple: (start_date_str, due_date_str) in YYYY-MM-DD format
    """
    launch_date = datetime.strptime(launch_date_str, "%Y-%m-%d")

    # Start Date = Launch Date - Days Before Launch
    start_date = launch_date - timedelta(days=days_before_launch)

    # Due Date = Start Date + Duration - 1
    if duration_days > 0:
        due_date = start_date + timedelta(days=duration_days - 1)
    else:
        # For milestones (0 duration), due date = start date
        due_date = start_date

    return start_date.strftime("%Y-%m-%d"), due_date.strftime("%Y-%m-%d")

def main():
    """Main execution function."""
    print("=" * 60)
    print("Asana Task Date Application Script")
    print("=" * 60)

    # Load data files
    print(f"\nLoading task GID mapping from: {TASK_GID_MAPPING}")
    gid_data = load_json(TASK_GID_MAPPING)
    task_gids = gid_data["task_mapping"]

    print(f"Loading task dates mapping from: {TASK_DATES_MAPPING}")
    dates_data = load_json(TASK_DATES_MAPPING)
    launch_date = dates_data["launch_date_anchor"]
    task_dates = dates_data["task_dates"]

    print(f"\nLaunch Date Anchor: {launch_date}")
    print(f"Total tasks to update: {len(task_gids)}")

    # Generate update plan
    updates = []
    missing_date_info = []

    for task_name, task_gid in task_gids.items():
        if task_name in task_dates:
            date_info = task_dates[task_name]
            days_before = date_info["days_before_launch"]
            duration = date_info["duration_days"]

            start_date, due_date = calculate_dates(launch_date, days_before, duration)

            updates.append({
                "task_name": task_name,
                "task_gid": task_gid,
                "start_on": start_date,
                "due_on": due_date,
                "days_before_launch": days_before,
                "duration_days": duration
            })
        else:
            missing_date_info.append(task_name)

    print(f"\nTasks with date calculations: {len(updates)}")
    print(f"Tasks missing date info: {len(missing_date_info)}")

    if missing_date_info:
        print("\nWARNING: Following tasks missing date information:")
        for task_name in missing_date_info:
            print(f"  - {task_name}")

    # Display sample updates
    print("\n" + "=" * 60)
    print("Sample Date Calculations (first 5 tasks)")
    print("=" * 60)
    for update in updates[:5]:
        print(f"\nTask: {update['task_name']}")
        print(f"  GID: {update['task_gid']}")
        print(f"  Days before launch: {update['days_before_launch']}")
        print(f"  Duration: {update['duration_days']} days")
        print(f"  Start date: {update['start_on']}")
        print(f"  Due date: {update['due_on']}")

    # Save update plan to file
    output_file = PROJECT_ROOT / "task_date_updates_plan.json"
    with open(output_file, 'w') as f:
        json.dump({
            "launch_date_anchor": launch_date,
            "total_updates": len(updates),
            "updates": updates,
            "missing_date_info": missing_date_info
        }, f, indent=2)

    print(f"\n" + "=" * 60)
    print(f"Update plan saved to: {output_file}")
    print("=" * 60)
    print("\nNext step: Execute API calls using the Asana MCP tools")
    print(f"Total API calls needed: {len(updates)}")

if __name__ == "__main__":
    main()
