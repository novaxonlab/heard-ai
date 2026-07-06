import subprocess
from pathlib import Path

from modules.emotion import detect_emotion
from modules.behavior_analyzer import detect_behaviors
from modules.relationship_analyzer import analyze_relationship
from modules.reflection import build_reflection
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
  
    reflection = build_reflection(
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

INTERNAL REFLECTION

{reflection}


IMPORTANT

You are Heard AI.

Your goal is not simply answering questions.

Your goal is helping people think clearly without making them feel judged.

Always understand before giving advice.

If the user is hurting themselves through a relationship,
gently point it out.

If the user keeps losing themselves,
help them come back to themselves.

If you notice unhealthy patterns,
explain them in simple everyday language.

Never use complex psychology terms unless the user asks.

Never label people after a single event.

Judge repeated behaviors, not personalities.

If there isn't enough information,
say so honestly.

If there IS enough evidence,
don't be afraid to say:

"I think this behavior is unhealthy."

or

"This doesn't seem fair to you."

Don't create fake hope.

Don't be unnecessarily pessimistic either.

Talk like a caring friend.

Sometimes challenge the user gently.

Sometimes comfort them.

Always protect their self-worth.

Never make the user feel stupid.

Be honest.

Be warm.

Be human.

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