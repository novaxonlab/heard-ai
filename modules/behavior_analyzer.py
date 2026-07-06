def detect_behaviors(text):
    """
    Heard AI Behavior Detection v2

    Finds emotional and relationship behavior patterns.
    """

    text = text.lower()

    behaviors = []

    # -------------------------
    # Checking Behaviors
    # -------------------------

    checking_words = [
        "instagram",
        "profil",
        "story",
        "hikaye",
        "son görülme",
        "çevrimiçi",
        "online",
        "hesabına baktım",
        "profiline baktım",
        "kaç kere baktım"
    ]

    if any(word in text for word in checking_words):
        behaviors.append("checking_behavior")

    # -------------------------
    # Waiting
    # -------------------------

    waiting_words = [
        "mesaj",
        "yazmadı",
        "neden yazmıyor",
        "bekliyorum",
        "geri döner mi",
        "görmesine rağmen"
    ]

    if any(word in text for word in waiting_words):
        behaviors.append("waiting_for_attention")

    # -------------------------
    # Overthinking
    # -------------------------

    overthinking_words = [
        "acaba",
        "ya",
        "belki",
        "çok düşünüyorum",
        "kafamdan çıkmıyor",
        "takıyorum"
    ]

    if any(word in text for word in overthinking_words):
        behaviors.append("overthinking")

    # -------------------------
    # Self Neglect
    # -------------------------

    self_neglect_words = [
        "kendimi unuttum",
        "her şeyim o oldu",
        "hayatım onun etrafında",
        "onsuz yapamam"
    ]

    if any(word in text for word in self_neglect_words):
        behaviors.append("self_neglect")

    # -------------------------
    # Jealousy
    # -------------------------

    jealousy_words = [
        "kıskanıyorum",
        "başkasıyla",
        "eski sevgilisi",
        "kimle konuşuyor"
    ]

    if any(word in text for word in jealousy_words):
        behaviors.append("jealousy")

    # -------------------------
    # Privacy
    # -------------------------

    privacy_words = [
        "telefonunu karıştırdım",
        "şifresini biliyorum",
        "hesabına girdim"
    ]

    if any(word in text for word in privacy_words):
        behaviors.append("privacy_violation")

    return behaviors