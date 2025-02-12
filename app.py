import streamlit as st
from src.chatbot import SimpleChatbot

# Initialize chatbot
bot = SimpleChatbot("data/intents.json")

# Title
st.title("💬 AI Chatbot - Enhanced Chat UI")
st.write("A simple AI-powered chatbot with a clean, built-in UI.")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history using Streamlit's built-in chat UI
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input box
user_input = st.text_input("Type your message here:", "")

if st.button("Send"):
    if user_input:
        response = bot.get_response(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()
