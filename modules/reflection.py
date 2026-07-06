def build_reflection(emotion, behaviors, relationship):
    """
    Creates internal guidance for Heard AI before generating a reply.
    """

    reflection = []

    # Emotion
    if emotion == "sad":
        reflection.append(
            "The user seems emotionally hurt. Respond with warmth first."
        )

    elif emotion == "anxious":
        reflection.append(
            "The user appears anxious. Help them slow down instead of feeding uncertainty."
        )

    elif emotion == "overwhelmed":
        reflection.append(
            "The user feels emotionally overwhelmed. Keep the response calm and simple."
        )

    # Behaviors
    if "checking_behavior" in behaviors:
        reflection.append(
            "The user is repeatedly checking the other person. Encourage them to focus on themselves."
        )

    if "self_neglect" in behaviors:
        reflection.append(
            "The user may be losing themselves in the relationship. Gently bring the conversation back to their own needs."
        )

    if "overthinking" in behaviors:
        reflection.append(
            "Do not increase overthinking. Help simplify the situation."
        )

    # Relationship
    if "one_sided_effort" in relationship:
        reflection.append(
            "The effort appears one-sided. Validate the user's feelings without attacking the other person."
        )

    if "possible_breadcrumbing" in relationship:
        reflection.append(
            "Explain what breadcrumbing is in simple language if it helps the user understand the pattern."
        )

    if "possible_gaslighting" in relationship:
        reflection.append(
            "Point out that the behavior seems emotionally unhealthy if supported by the conversation."
        )

    if "self_worth_risk" in relationship:
        reflection.append(
            "Prioritize protecting the user's self-worth."
        )

    if not reflection:
        reflection.append(
            "Listen carefully before giving advice."
        )

    return "\n".join(reflection)