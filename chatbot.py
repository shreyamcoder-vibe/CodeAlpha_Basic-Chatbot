print("Chatbot is running...")
print("Type 'bye' to exit.")
while True:
    user_input = input("You: ").lower()
    if user_input == "hello":
        print("Bot: Hi! ")
    elif user_input == "how are you":
        print("Bot: I am fine, thanks for asking !!")
    elif user_input == "bye":
        print("Bot: Goodbye! Have a nice day ")
        break
    else:
        print("Bot: Sorry, I don't understand that.")
