import random
import responsesListe


def chatbotRespons(user_input):
    responses = {
        "bonjour": random.choice(responsesListe.greetings),
        "comment ça va ?": random.choice(responsesListe.take_news),
        "a bientôt": "A plus",
        "quit": "A bientôt"
    }
    return responses.get(user_input)



# Communication avec le ChatBot
while True:
    user_sms = input("Vous: ")

    if user_sms != "quit":
        print("chat:",chatbotRespons(user_sms.lower()))
    else:
        print("A bientôt !")
        break