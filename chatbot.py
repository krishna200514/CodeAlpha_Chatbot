def chatbot():
    print("Bot: Hello! I’m your basic chatbot. Let’s chat! (Type 'bye' to exit)")
    
    name = ""  # variable to store user's name

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hi", "hello", "hey", "hii", "hello chatbot"]:
            print("Bot: Hi there! 👋 How are you doing?")
        
        elif user_input in ["i'm fine", "i am fine", "good", "fine", "doing well"]:
            print("Bot: That’s great to hear! 😊 What’s your name?")
            name = input("You: ").strip().capitalize()
            print(f"Bot: Nice to meet you, {name}!")
            print("Bot: Do you like chatting with me? (yes/no)")
        
        elif user_input == "yes":
            print("Bot: Yay! I'm glad to hear that 😊")
        
        elif user_input == "no":
            print("Bot: Oh no! I'll try to get better 😔")

        elif user_input == "how are you":
            print("Bot: I'm just a program, but I’m doing great! 😄")

        elif user_input == "bye":
            if name:
                print(f"Bot: Goodbye, {name}! Have a wonderful day! 👋")
            else:
                print("Bot: Goodbye! Have a wonderful day! 👋")
            break

        else:
            print("Bot: Hmm... I didn’t understand that. Can you try saying it differently?")

# Start the chatbot
chatbot()
