from datetime import datetime
from pathlib import Path
from zoneinfo import ZoneInfo

import holidays

ROOT = Path(__file__).resolve().parents[1]
OUTPUT_DIR = ROOT / "daily-challenges"

today = datetime.now(ZoneInfo("Asia/Kolkata")).date()

# National Indian holidays + Telangana holidays
india_holidays = holidays.country_holidays(
    "IN",
    subdiv="TS",
    years=[today.year],
)

if today in india_holidays:
    print(f"Holiday: {india_holidays[today]}. Skipping today's challenge.")
    raise SystemExit(0)

challenges = [
    (
        "Python Dictionaries",
        "Write a function that returns the frequency of every word in a string."
    ),
    (
        "SQL Window Functions",
        "Find the second-highest salary in an employee table, handling ties."
    ),
    (
        "PySpark Deduplication",
        "Remove duplicate customer records while retaining the latest record."
    ),
    (
        "SQL Data Quality",
        "Find duplicate customer IDs and report their occurrence counts."
    ),
    (
        "Airflow Reliability",
        "Explain how to make a daily ETL task safe to retry without duplicating data."
    ),
    (
        "SCD Type 2",
        "Design SQL logic to preserve historical changes to customer records."
    ),
    (
        "Python Data Processing",
        "Process a large CSV file in chunks and count invalid records."
    ),
    (
        "Spark Performance",
        "Explain how you would investigate and mitigate data skew in a Spark job."
    ),
    (
        "SQL Analytics",
        "Calculate a rolling seven-day revenue total using a window function."
    ),
    (
        "Pipeline Testing",
        "Write tests for schema validity, null values, duplicates, and row counts."
    ),
]

# Rotate through the challenge collection across the year.
challenge = challenges[(today.timetuple().tm_yday - 1) % len(challenges)]

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
file_path = OUTPUT_DIR / f"{today.isoformat()}.md"

if file_path.exists():
    print(f"Challenge already exists: {file_path.name}")
    raise SystemExit(0)

title, task = challenge

content = f"""# Daily Coding Challenge — {today.isoformat()}

## Topic
{title}

## Problem
{task}

## Your work
- [ ] Implement the solution.
- [ ] Test normal cases and edge cases.
- [ ] Add time/space complexity or performance considerations.
- [ ] Commit the solution after testing.

## Solution
Add your implementation and explanation in a separate file.
"""

file_path.write_text(content, encoding="utf-8")
print(f"Created challenge: {file_path}")