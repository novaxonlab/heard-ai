import json
from pathlib import Path

MEMORY_FILE = Path("memories/user_memory.json")


def load_memory():
    if not MEMORY_FILE.exists():
        return {"history": []}

    with open(MEMORY_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_memory(memory):
    MEMORY_FILE.parent.mkdir(exist_ok=True)

    with open(MEMORY_FILE, "w", encoding="utf-8") as f:
        json.dump(memory, f, ensure_ascii=False, indent=4)


def remember(user_message, ai_reply):
    memory = load_memory()

    memory["history"].append({
        "user": user_message,
        "heard": ai_reply
    })

    # Son 20 konuşmayı tut
    memory["history"] = memory["history"][-20:]

    save_memory(memory)


def get_recent_history():
    memory = load_memory()

    return memory["history"]