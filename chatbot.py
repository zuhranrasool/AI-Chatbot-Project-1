# -----------------------------------------
# AI Chatbot Project 1
# Decode Labs AI Internship
# Author: Zuhran Rasool
# -----------------------------------------

print("=" * 50)
print("      Welcome to AI Rule-Based Chatbot")
print("=" * 50)

print("Hello! I am your AI Chatbot.")
print("I can answer simple predefined questions.")
print("Type 'help' to see available commands.")
print("Type 'bye' anytime to exit the chatbot.")
print("=" * 50)

while True:
    user = input("\nYou: ")
    user = user.lower()

    if user == "hi":
        print("Chatbot: Hi! Nice to meet you.")

    elif user == "hello":
        print("Chatbot: Hello! How can I assist you today?")

    elif user == "hey":
        print("Chatbot: Hey! Hope you're having a great day.")

    elif user == "good morning":
        print("Chatbot: Good morning! Wishing you a wonderful day ahead.")

    elif user == "good evening":
        print("Chatbot: Good evening! Hope you had a productive day.")

    elif user == "how are you":
        print("chatbot:I'm doing great! Thanks for asking. How can I help you today?")

    elif user == "what is your name":
        print("Chatbot: My name is AI Chatbot. I was created as part of the Decode Labs AI Internship Project.")

    elif user == "who are you":
        print("Chatbot: I am a rule-based AI chatbot designed to answer predefined questions.")

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