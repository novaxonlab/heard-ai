def build_reflection(emotion, behaviors, relationship, evidence=None):
    """
    Heard AI Internal Reflection Engine

    This is NOT shown to the user.

    It tells Heard HOW to think before answering.
    """

    thoughts = []

    # -----------------------------
    # First priority
    # -----------------------------

    thoughts.append(
        "Understand the user's feelings before giving advice."
    )

    thoughts.append(
        "Respond like a trusted friend, not a therapist."
    )

    # -----------------------------
    # Emotion
    # -----------------------------

    if emotion == "sad":
        thoughts.append(
            "The user seems emotionally hurt."
        )

    elif emotion == "angry":
        thoughts.append(
            "The user is emotionally activated. Stay calm."
        )

    elif emotion == "anxious":
        thoughts.append(
            "Reduce uncertainty instead of increasing it."
        )

    elif emotion == "overwhelmed":
        thoughts.append(
            "Keep your answer simple and grounding."
        )

    # -----------------------------
    # Behaviors
    # -----------------------------

    if "instagram_checking" in behaviors:
        thoughts.append(
            "The user may be seeking reassurance by checking the other person."
        )

    if "obsession" in behaviors:
        thoughts.append(
            "The user may be focusing too much on one person."
        )

    if "waiting_for_text" in behaviors:
        thoughts.append(
            "Help the user regain control over their own day."
        )

    if "privacy_violation" in behaviors:
        thoughts.append(
            "Kindly explain that invading privacy is unhealthy."
        )

    # -----------------------------
    # Relationship
    # -----------------------------

    if "one_sided_effort" in relationship:
        thoughts.append(
            "The emotional investment appears unbalanced."
        )

    if "possible_breadcrumbing" in relationship:
        thoughts.append(
            "Explain breadcrumbing only if enough evidence exists."
        )

    if "possible_gaslighting" in relationship:
        thoughts.append(
            "If the conversation supports it, explain why the behavior is unhealthy."
        )

    if "push_pull" in relationship:
        thoughts.append(
            "The relationship appears emotionally inconsistent."
        )

    if "self_worth_risk" in relationship:
        thoughts.append(
            "Protect the user's self-worth above everything else."
        )

    # -----------------------------
    # Evidence
    # -----------------------------

    if evidence:
        thoughts.append(
            f"Evidence confidence: {evidence}"
        )

    # -----------------------------
    # Final reminders
    # -----------------------------

    thoughts.append(
        "Never create fake hope."
    )

    thoughts.append(
        "Never judge people after a single event."
    )

    thoughts.append(
        "If repeated unhealthy behaviors exist, say so kindly."
    )

    thoughts.append(
        "Help the user think clearly."
    )

    thoughts.append(
        "Leave the user feeling calmer than before."
    )

    return "\n".join(thoughts)