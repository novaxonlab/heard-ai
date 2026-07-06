def detect_emotion(text):
    """
    Heard AI Emotion Detection v2

    Returns:
        sad
        anxious
        angry
        happy
        confused
        hopeful
        overwhelmed
        neutral
    """

    text = text.lower()

    emotions = {
        "sad": [
            "üzgün",
            "ağlıyorum",
            "kötüyüm",
            "yoruldum",
            "bittim",
            "değersiz",
            "canım çok yanıyor",
            "kalbim kırıldı",
            "üzülüyorum"
        ],

        "anxious": [
            "acaba",
            "ya yazmazsa",
            "ya istemiyorsa",
            "takıyorum",
            "stres",
            "kaygı",
            "korkuyorum",
            "sürekli düşünüyorum",
            "kafama takıyorum",
            "bekliyorum"
        ],

        "angry": [
            "sinirliyim",
            "nefret ediyorum",
            "delirdim",
            "çok sinirlendim",
            "beni çıldırttı"
        ],

        "happy": [
            "çok mutluyum",
            "harika hissediyorum",
            "çok sevindim",
            "iyi hissediyorum",
            "bugün güzel geçti"
        ],

        "confused": [
            "anlamıyorum",
            "kararsızım",
            "kafam karışık",
            "emin değilim",
            "ne yapacağımı bilmiyorum"
        ],

        "hopeful": [
            "belki düzelir",
            "umut ediyorum",
            "belki yazar",
            "şans vermek istiyorum"
        ],

        "overwhelmed": [
            "her şey üstüme geliyor",
            "boğuluyorum",
            "çok bunaldım",
            "artık dayanamıyorum"
        ]
    }

    scores = {}

    for emotion, keywords in emotions.items():
        scores[emotion] = sum(1 for keyword in keywords if keyword in text)

    if max(scores.values()) == 0:
        return "neutral"

    return max(scores, key=scores.get)