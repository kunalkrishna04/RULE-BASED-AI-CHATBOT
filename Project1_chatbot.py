# Rule-Based AI Chatbot
# DecodeLabs Internship Project 1

print("===================================")
print(" Welcome to AI Chatbot ")
print("===================================")
print("Type 'bye' to exit.\n")

while True:
    
    user = input("You: ").lower().strip()

    if user in ["hi", "hello", "hey"]:
        print("Bot: Hello! How can I help you?")

    elif user == "how are you":
        print("Bot: I am fine. Thanks for asking!")

    elif user == "what is your name":
        print("Bot: My name is AI Chatbot.")

    elif user == "who made you":
        print("Bot: I was created using Python.")

    elif user == "what is ai":
        print("Bot: AI stands for Artificial Intelligence.")

    elif user == "what is python":
        print("Bot: Python is a popular programming language.")

    elif user == "why learn python":
        print("Bot: Python is easy to learn and widely used in AI and software development.")

    elif user == "what is coding":
        print("Bot: Coding means giving instructions to a computer.")

    elif user == "what is btech":
        print("Bot: BTech stands for Bachelor of Technology.")

    elif user == "your favorite language":
        print("Bot: Python is my favorite language.")

    elif user in ["thanks", "thank you"]:
        print("Bot: You're welcome!")

    elif user == "bye":
        print("Bot: Goodbye! Have a great day.")
        break

    else:
        print("Bot: Sorry, I don't understand that question.")