import json
from pathlib import Path

PROFILE_FILE = Path("memories/user_profile.json")


def load_profile():
    if not PROFILE_FILE.exists():
        return {}

    with open(PROFILE_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_profile(profile):
    PROFILE_FILE.parent.mkdir(exist_ok=True)

    with open(PROFILE_FILE, "w", encoding="utf-8") as f:
        json.dump(profile, f, ensure_ascii=False, indent=4)