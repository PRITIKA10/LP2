import random
import re

# Define a dictionary of responses based on keywords
responses = {
    'hello': ["Hello!", "Hi there!", "Hey!", "Hi!"],
    'how are you': ["I'm a bot, but I'm good. How about you?", "I'm just a program, but I'm doing well!"],
    'bye': ["Goodbye!", "See you later!", "Bye! Have a great day!"],
    'default': ["I'm not sure I understand. Could you rephrase that?", "Sorry, I don't get it."]
}

# Simple function to get a response based on user input
def get_response(user_input):
    user_input = user_input.lower()  # Make input lowercase
    for key in responses:
        if key in user_input:  # Check if keyword is in user input
            return random.choice(responses[key])  # Return a random response from the corresponding list
    return random.choice(responses['default'])  # Return a default response if no keyword is found

# Run a simple conversation loop
def chatbot():
    print("Welcome to the chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if 'bye' in user_input.lower():  # Exit if user says 'bye'
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)  # Get a response based on user input
        print(f"Chatbot: {response}")

# Start the chatbot
chatbot()
