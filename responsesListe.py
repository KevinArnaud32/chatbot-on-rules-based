from datetime import datetime


date_time_now = datetime.now().time().strftime("%H:%M")

greetings = (
        "Salut",
        "Bonjour !!!",
        "Bonjour ! Comment vous allez ?",
        "Bonjour vous allez bien j'espère ?",
        "Bonjour ! Comment pourrais-je vous aider ?",
        "Bonjour ! Comment puis-je vous aider aujourd'hui ?",
        "Salut ! Que puis-je faire pour vous ?",
        "Hello ! Comment allez- vous ?",
        "Bonjour, comment ça va ?",
        "Salut ! En quoi puis-je être utile ?",
        "Bonjour, ravi de vous voir ici !",
        "Hey, bonjour ! Comment puis-je vous assister ?",
        "Salut, bonjour ! Qu'est-ce que je peux faire pour vous ?",
        "Bonjour, je suis là pour vous aider !",
        "Bonjour, comment puis-je rendre votre journée meilleure ?"
    )

take_news = (
    "Je vais bien, merci de demander ! Et vous ?",
    "Ça va très bien, merci ! Et toi ?",
    "Tout va bien, merci ! Comment vas-tu ?",
    "Je vais bien, merci ! Et toi, comment ça va ?",
    "Ça va super, merci ! Et toi, comment te sens-tu ?",
    "Je vais bien, merci ! Et toi, tout va bien ?",
    "Ça va, merci ! Et toi, comment ça roule ?",
    "Tout va bien de mon côté, merci ! Et toi ?",
    "Je vais bien, merci pour ta question ! Et toi ?",
    "Tout va pour le mieux, merci ! Et toi, comment vas-tu ?"
)

reponses_heure = (
    f"{date_time_now}",
    f"il est {date_time_now}",
    f"L'heure exacte dépend de ton fuseau horaire. il est peut être {date_time_now}",
    f"Si tu veux l'heure exacte, il est {date_time_now}",
    f"Le temps passe vite ! il est exactement {date_time_now}",
    f"il est peut être {date_time_now}"
)
