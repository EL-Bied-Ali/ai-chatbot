from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

class SimpleChatbot:
    def __init__(self):
        # Load Mistral's "Le Chat" model and tokenizer
        self.tokenizer = AutoTokenizer.from_pretrained("mistralai/le-chat")
        self.model = AutoModelForCausalLM.from_pretrained("mistralai/le-chat")

    def get_response(self, user_input):
        """Generate a response using the AI model."""
        inputs = self.tokenizer.encode(user_input + self.tokenizer.eos_token, return_tensors="pt")
        outputs = self.model.generate(inputs, max_length=100, pad_token_id=self.tokenizer.eos_token_id)
        response = self.tokenizer.decode(outputs[0], skip_special_tokens=True)
        return response

# Example usage
if __name__ == "__main__":
    bot = SimpleChatbot()
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Chatbot: Goodbye!")
            break
        print("Chatbot:", bot.get_response(user_input))
