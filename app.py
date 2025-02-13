import streamlit as st
from src.chatbot import SimpleChatbot

# Initialize chatbot
bot = SimpleChatbot()

st.title("💬 AI Chatbot - Demo")
st.write("A simple AI-powered chatbot demo. Type your message and press Enter!")

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.write(f"**You:** {message['content']}")
    else:
        st.write(f"**Chatbot:** {message['content']}")

# Chat input form
user_input = st.text_input("Your message:")
if user_input:
    response = bot.get_response(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})
    st.session_state.messages.append({"role": "assistant", "content": response})
    st.experimental_rerun()
