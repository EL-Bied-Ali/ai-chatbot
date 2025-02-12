import streamlit as st
from src.chatbot import SimpleChatbot

# Initialize chatbot
bot = SimpleChatbot("data/intents.json")

# Streamlit UI
st.title("💬 AI Chatbot")
st.write("A simple AI-powered chatbot built with Python and NLP.")

user_input = st.text_input("You:", "")

if st.button("Send"):
    response = bot.get_response(user_input)
    st.write(f"🤖 Chatbot: {response}")
