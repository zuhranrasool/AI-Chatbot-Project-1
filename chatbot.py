from datetime import datetime

# -----------------------------------------
# AI Chatbot Project 1
# Decode Labs AI Internship
# Author: Zuhran Rasool
# -----------------------------------------

# Display the welcome message
print("=" * 50)
print("      Welcome to AI Rule-Based Chatbot")
print("=" * 50)

print("Hello! I am your AI Chatbot.")
print("I can answer simple predefined questions.")
print("Type 'help' to see available commands.")
print("Type 'bye' anytime to exit the chatbot.")
print("=" * 50)

# Start the chatbot conversation
while True:

    # Take user input and convert it to lowercase
    user = input("\nYou: ")
    user = user.lower()

    # Handle greeting commands
    if user == "hi":
        print("Chatbot: Hi! Nice to meet you. How can I assist you today?")

    elif user == "hello":
        print("Chatbot: Hello! Welcome! How can I help you today?")

    elif user == "hey":
        print("Chatbot: Hey! It's great to see you. How can I help?")

    elif user == "good morning":
        print("Chatbot: Good morning! I hope you have a wonderful and productive day.")

    elif user == "good evening":
        print("Chatbot: Good evening! I hope you're having a relaxing evening.")

    # Handle "How are you?" command
    elif user == "how are you":
        print("Chatbot: I'm doing great! Thanks for asking. I'm always ready to help you.")

    # Handle chatbot identity questions
    elif user == "what is your name":
        print("Chatbot: My name is AI Chatbot. I was developed as part of the Decode Labs AI Internship Project.")

    elif user == "who are you":
        print("Chatbot: I am a rule-based AI chatbot designed to answer predefined questions and assist users.")

    # Display the help menu
    elif user == "help" or user == "commands" or user == "menu":
        print("\n========== Available Commands ==========")
        print("• hi")
        print("• hello")
        print("• hey")
        print("• good morning")
        print("• good evening")
        print("• how are you")
        print("• what is your name")
        print("• who are you")
        print("• date")
        print("• time")
        print("• thanks")
        print("• thank you")
        print("• bye")
        print("========================================")

    # Display the current date
    elif user == "date":
        today = datetime.now().strftime("%d-%m-%Y")
        print(f"Chatbot: Today's date is {today}")

    # Display the current time
    elif user == "time":
        current_time = datetime.now().strftime("%I:%M:%S %p")
        print(f"Chatbot: The current time is {current_time}")

    # Handle thank you messages
    elif user == "thanks":
        print("Chatbot: You're very welcome! I'm always happy to help.")

    elif user == "thank you" or user == "thankyou":
        print("Chatbot: You're most welcome! Feel free to ask if you need anything else.")

    # Exit the chatbot
    elif user == "bye" or user == "goodbye" or user == "exit" or user == "quit":
        print("Chatbot: Goodbye! Thank you for chatting with me. Have a wonderful day!")
        break

    # Handle unknown commands
    else:
        print("Chatbot: Sorry, I couldn't understand your request.")
        print("Chatbot: Please type 'help' to see the list of available commands.")