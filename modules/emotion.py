def detect_emotion(text):
    """
    İlk sürüm: Basit duygu analizi.
    Daha sonra bunu gerçek AI modeliyle değiştireceğiz.
    """

    text = text.lower()

    emotions = {
        "sad": [
            "üzgün",
            "ağlıyorum",
            "kötüyüm",
            "çok kötü",
            "yoruldum",
            "bittim",
            "değersiz"
        ],

        "angry": [
            "sinir",
            "nefret",
            "delirdim",
            "aptal",
            "gerizekalı"
        ],

        "anxious": [
            "ya",
            "acaba",
            "takıyorum",
            "kaygı",
            "stres",
            "korkuyorum"
        ],

        "happy": [
            "çok mutluyum",
            "harika",
            "iyi hissediyorum",
            "sevindim"
        ]
    }

    scores = {}

    for emotion, words in emotions.items():
        scores[emotion] = sum(word in text for word in words)

    if not any(scores.values()):
        return "neutral"

    return max(scores, key=scores.get)