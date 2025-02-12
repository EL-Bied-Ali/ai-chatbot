import streamlit as st
import spacy
import subprocess
from src.chatbot import SimpleChatbot

# Ensure spaCy model is installed
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    subprocess.run(["python", "-m", "spacy", "download", "en_core_web_sm"])
    nlp = spacy.load("en_core_web_sm")

# Initialize chatbot
bot = SimpleChatbot("data/intents.json")

# Streamlit UI
st.title("💬 AI Chatbot")
st.write("A simple AI-powered chatbot built with Python and NLP.")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    st.write(message)

# User input box
user_input = st.text_input("You:", "")

if st.button("Send"):
    if user_input:
        response = bot.get_response(user_input)
        st.session_state.messages.append(f"🧑 You: {user_input}")
        st.session_state.messages.append(f"🤖 Chatbot: {response}")

        # Display updated chat history
        for message in st.session_state.messages:
            st.write(message)
