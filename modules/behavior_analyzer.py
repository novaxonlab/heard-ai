def detect_behaviors(text):
    """
    Kullanıcının davranış kalıplarını bulur.
    """

    text = text.lower()

    behaviors = []

    if "instagram" in text:
        behaviors.append("instagram_checking")

    if "profil" in text:
        behaviors.append("profile_checking")

    if "mesaj" in text:
        behaviors.append("waiting_for_text")

    if "takıntı" in text:
        behaviors.append("obsession")

    if "sürekli" in text:
        behaviors.append("repetitive_behavior")

    if "telefonunu karıştırdım" in text:
        behaviors.append("privacy_violation")

    return behaviors