import json
import random
import spacy
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class SimpleChatbot:
    def __init__(self, intents_file):
        self.intents = self.load_intents(intents_file)
        self.nlp = spacy.load("en_core_web_sm")
        self.vectorizer = TfidfVectorizer()
        self.train_intent_vectors()
        self.memory = {"last_intent": None, "last_response": None}  # Store context

    def load_intents(self, filename):
        """Load chatbot intents from a JSON file."""
        with open(filename, "r") as file:
            return json.load(file)["intents"]

    def train_intent_vectors(self):
        """Precompute TF-IDF vectors for all intent patterns."""
        self.intent_patterns = []
        self.intent_tags = []
        for intent in self.intents:
            for pattern in intent["patterns"]:
                self.intent_patterns.append(pattern)
                self.intent_tags.append(intent["tag"])
        if self.intent_patterns:
            self.tfidf_matrix = self.vectorizer.fit_transform(self.intent_patterns)

    def get_best_intent(self, user_input):
        """Find the most similar intent using cosine similarity."""
        user_vector = self.vectorizer.transform([user_input])
        similarity_scores = cosine_similarity(user_vector, self.tfidf_matrix)
        best_match_idx = np.argmax(similarity_scores)
        threshold = 0.25  # Lower threshold for informal phrases
        return self.intent_tags[best_match_idx] if similarity_scores[0][best_match_idx] > threshold else None

    def get_response(self, user_input):
        """Generate a response with context awareness."""
        user_input_lower = user_input.lower().strip()
        best_intent = self.get_best_intent(user_input)

        # Check for follow-up triggers
        follow_up_triggers = ["what else", "and", "more", "anything else", "other things"]
        if any(trigger in user_input_lower for trigger in follow_up_triggers):
            if self.memory["last_intent"]:
                # For follow-ups, try to provide a different response for the last intent.
                for intent in self.intents:
                    if intent["tag"] == self.memory["last_intent"]:
                        responses = [resp for resp in intent["responses"] if resp != self.memory["last_response"]]
                        if responses:
                            chosen = random.choice(responses)
                            self.memory["last_response"] = chosen
                            return chosen
                        else:
                            return "I've already mentioned the main points. Anything specific you're curious about?"
            else:
                return "Could you clarify what topic you're referring to?"

        # For non-follow-up queries
        if best_intent:
            for intent in self.intents:
                if intent["tag"] == best_intent:
                    chosen = random.choice(intent["responses"])
                    self.memory["last_intent"] = best_intent
                    self.memory["last_response"] = chosen
                    return chosen

        return "I'm not sure I understand. Can you rephrase?"

if __name__ == "__main__":
    bot = SimpleChatbot("data/intents.json")
    while True:
        user_text = input("You: ")
        if user_text.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", bot.get_response(user_text))
