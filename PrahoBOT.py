import random


responses = {
    "hi": ["Hello!", "Hi there!", "Hey!"],
    "how are you?": ["I'm good, thank you!", "Feeling great, thanks!"],
    "what's your name?": ["I'm just a simple chatbot.", "You can call me Chatbot!"],
    "bye": ["Goodbye!", "See you later!", "Bye!"],
    "default": ["I'm not sure what you mean.", "Could you please rephrase that?", "Sorry, I didn't catch that."],
}


def chatbot(message):

    message = message.lower()


    if message in responses:
        return random.choice(responses[message])
    else:
        return random.choice(responses["default"])


def main():
    print("Hello! I'm your chatbot. You can start chatting. Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print(chatbot("bye"))
            break
        else:
            print("Chatbot:", chatbot(user_input))


if __name__ == "__main__":
    main()
