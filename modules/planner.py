"""
Heard AI Planner

Bu modül cevap yazmaz.

Bu modül sadece düşünür.

Diğer modüllerden gelen bilgileri bir araya getirir
ve Heard'ın nasıl cevap vermesi gerektiğine karar verir.
"""


def create_plan(user_message, emotion, behaviors, relationship):
    plan = {
        "emotion": emotion,
        "behaviors": behaviors,
        "relationship": relationship,

        # Heard nasıl konuşmalı?
        "tone": "friend",

        # Cevabın amacı
        "goal": "help_user",

        # Bunları ASLA yapma
        "avoid": [
            "judge",
            "diagnose",
            "fake_hope",
            "attack_other_person"
        ],

        # Bunları yap
        "focus": [
            "understand_feelings",
            "protect_self_worth",
            "be_honest",
            "stay_kind"
        ]
    }

    return plan