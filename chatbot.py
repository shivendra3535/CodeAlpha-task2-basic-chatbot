import nltk
from nltk.chat.util import Chat, reflections

pairs= [
    [
        r"my name is (.*)",
        ["Hello %1 ! How can i help you today?", "Hii there %1 ! what can i do for you"],             
    ],
    [
        r"what is your name?",
        ["I am chatbot. You can call me CodeAlpha_GPT", "I don't have name, you can call me CodeAlpha_GPT"],

    ],
    [
        r"how are you",
        ["i am doing well, thank you!", "I'm just a computer program, so I don't have feelings, but I'm here to help."],

    ],
    [
        r"(.*) your age?",
        ["I don't have an age. I'm just a computer program.", "Age is not applicable to me."],
    ],
    [
        r"what can you do",
        ["I can assist you with general queries. Feel free to ask me anything.", "I'm here to help. Ask me anything you'd like."],
    ],
    [
        r"quit",
        ["Bye! Take care.", "Goodbye! If you have more questions, feel free to ask."],
    ],
    ]

chatbot= Chat(pairs, reflections)

def chat():
    print("Hello i am CodeAlpha chatbot. Type 'quit' to exit.")
    while True:
        user_input= input("you : ")
        if user_input.lower()=='quite' :
            print("Chatbot : bye! take care.")
            break
        else :
            response= chatbot.respond(user_input)
            print("chatbot : ", response)

if __name__ == "__main__" :
    nltk.download("puntk")
    chat() 