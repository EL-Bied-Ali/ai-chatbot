import json
import random
import spacy

class SimpleChatbot:
    def __init__(self, intents_file):
        self.intents = self.load_intents(intents_file)
        self.nlp = spacy.load("en_core_web_sm")  # Using spaCy for NLP

    def load_intents(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)
        return data["intents"]

    def get_response(self, user_input):
        user_input_lower = user_input.lower()

        # Simple approach: check if user_input contains a pattern
        for intent in self.intents:
            for pattern in intent["patterns"]:
                if pattern.lower() in user_input_lower:
                    return random.choice(intent["responses"])

        # If no pattern matched
        return "I'm not sure I understand. Can you rephrase?"

# Testing in CLI
if __name__ == "__main__":
    bot = SimpleChatbot("data/intents.json")
    while True:
        user_text = input("You: ")
        if user_text.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", bot.get_response(user_text))
