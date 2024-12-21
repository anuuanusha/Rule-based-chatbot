def chatbot():
    print("Hi! I'm your rule-based chatbot. How can I assist you today?")
    print("(Type 'exit' to end the conversation)")

    while True:
        user_input = input("You: ").lower()

        # Exit condition
        if user_input == 'exit':
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Responses based on rules
        if "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you today?")
        elif "how are you" in user_input:
            print("Chatbot: I'm just a bot, but I'm functioning as expected! How about you?")
        elif "your name" in user_input:
            print("Chatbot: I'm a simple rule-based chatbot. What's your name?")
        elif "weather" in user_input:
            print("Chatbot: I can't check the weather, but it's always a good idea to keep an umbrella handy!")
        elif "help" in user_input:
            print("Chatbot: Sure! Let me know what you need help with.")
        elif "bye" in user_input:
            print("Chatbot: Goodbye! Take care!")
            break
        else:
            print("Chatbot: I'm sorry, I didn't understand that. Could you rephrase?")

# Run the chatbot
chatbot()
