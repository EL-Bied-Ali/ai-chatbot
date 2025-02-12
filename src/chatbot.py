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
        self.vectorizer = TfidfVectorizer()  # TF-IDF model
        self.train_intent_vectors()

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
        """Find the most similar intent to the user input using cosine similarity."""
        user_vector = self.vectorizer.transform([user_input])
        similarity_scores = cosine_similarity(user_vector, self.tfidf_matrix)
        best_match_idx = np.argmax(similarity_scores)

        return self.intent_tags[best_match_idx] if similarity_scores[0][best_match_idx] > 0.3 else None  # Threshold

    def get_response(self, user_input):
        """Get the best chatbot response based on intent similarity."""
        best_intent = self.get_best_intent(user_input)

        if best_intent:
            for intent in self.intents:
                if intent["tag"] == best_intent:
                    return random.choice(intent["responses"])
        
        return "I'm not sure I understand. Can you rephrase?"

if __name__ == "__main__":
    bot = SimpleChatbot("data/intents.json")
    while True:
        user_text = input("You: ")
        if user_text.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", bot.get_response(user_text))
