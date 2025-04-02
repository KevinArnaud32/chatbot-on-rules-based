import random
import responsesListe


def chatbotRespons(user_input):
    responses = {
        "bonjour": random.choice(responsesListe.greetings),
        "comment ça va ?": random.choice(responsesListe.take_news),
        "il fait quelle heure ?": random.choice(responsesListe.reponses_heure),
        "quit": "A bientôt",
    }
    return responses.get(user_input)



# Communication chatbot - user
while True:
    user_sms = input("Vous: ")

    if user_sms.lower() != "quit":
        print("chat:",chatbotRespons(user_sms.lower().strip()))
    else:
        print("chat:", chatbotRespons(user_sms.lower().strip()))
        break