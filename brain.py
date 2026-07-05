import subprocess
from pathlib import Path

from modules.emotion import detect_emotion
from modules.behavior_analyzer import detect_behaviors
from modules.relationship_analyzer import analyze_relationship
from modules.planner import create_plan
from modules.memory import remember, get_recent_history


def load_knowledge(filename):
    path = Path("knowledge") / filename

    if path.exists():
        return path.read_text(encoding="utf-8")

    return ""


PERSONALITY = load_knowledge("personality.md")
VALUES = load_knowledge("values.md")
COMMUNICATION = load_knowledge("communication.md")
PATTERNS = load_knowledge("relationship_patterns.md")
FLAGS = load_knowledge("red_green_flags.md")
SCENARIOS = load_knowledge("scenarios.md")


def get_response(user_input):

    # -------------------------
    # Heard Intelligence Engine
    # -------------------------

    emotion = detect_emotion(user_input)

    behaviors = detect_behaviors(user_input)

    relationship = analyze_relationship(user_input)

    plan = create_plan(
        user_input,
        emotion,
        behaviors,
        relationship
    )

    history = get_recent_history()

    system_prompt = f"""
You are Heard AI.

============================

PERSONALITY

{PERSONALITY}

============================

VALUES

{VALUES}

============================

COMMUNICATION

{COMMUNICATION}

============================

RELATIONSHIP KNOWLEDGE

{PATTERNS}

============================

RED & GREEN FLAGS

{FLAGS}

============================

SCENARIOS

{SCENARIOS}

============================

RECENT CONVERSATIONS

{history}

============================

CURRENT ANALYSIS

Emotion:
{emotion}

Behaviors:
{behaviors}

Relationship:
{relationship}

Plan:
{plan}

============================

IMPORTANT

You are Heard AI.

Talk like a close friend.

Never sound robotic.

Never sound like ChatGPT.

Never sound like customer support.

Never use complicated psychology words.

Never diagnose people.

Judge behaviors, not personalities.

If the user is wrong,
say it kindly.

If the other person seems unhealthy,
explain why the behavior is concerning.

Don't give false hope.

Don't exaggerate.

Keep your answers natural.

Short answers are usually better.

Help the user remember themselves.

"""

    prompt = f"""
{system_prompt}

User:

{user_input}

Heard:
"""

    try:

        result = subprocess.run(
            ["ollama", "run", "llama3", prompt],
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            return result.stderr

        reply = result.stdout.strip()

        remember(user_input, reply)

        return reply

    except Exception as e:
        return str(e)