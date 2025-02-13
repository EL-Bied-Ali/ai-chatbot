from transformers import pipeline

class SimpleChatbot:
    def __init__(self):
        # Load a pre-trained conversational model
        self.chatbot = pipeline("conversational", model="facebook/blenderbot-400M-distill")

    def get_response(self, user_input):
        """Generate a response using a conversational AI model."""
        conversation = self.chatbot(user_input)
        return conversation[0]["generated_text"]

# Example usage
if __name__ == "__main__":
    bot = SimpleChatbot()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", bot.get_response(user_input))
