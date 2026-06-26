def chatbot():

    print("----- Welcome to Simple Chatbot -----")
    print("Type 'bye' to end the chat\n")

    while True:
        message = input("You: ").lower()

        if message == "hello":
            print("Bot: Hi!")

        elif message == "how are you":
            print("Bot: I'm fine, thanks!")

        elif message == "what is your name":
            print("Bot: My name is ChatBot.")

        elif message == "who created you":
            print("Bot: I was created using Python.")

        elif message == "good morning":
            print("Bot: Good morning! Have a great day.")

        elif message == "good evening":
            print("Bot: Good evening!")

        elif message == "what are you doing":
            print("Bot: I am chatting with you.")

        elif message == "tell me a joke":
            print("Bot: Why do programmers prefer dark mode? Because light attracts bugs!")

        elif message == "thank you":
            print("Bot: You're welcome!")

        elif message == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

# Calling function
chatbot()