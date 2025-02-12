import streamlit as st
from src.chatbot import SimpleChatbot

# Initialize chatbot
bot = SimpleChatbot("data/intents.json")

st.title("💬 AI Chatbot - Enhanced")
st.write("A simple AI-powered chatbot with a built-in chat UI. Press Enter to send your message!")

# Initialize chat history in session state if not already present
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history using Streamlit's built-in chat UI
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.write(message["content"])
    else:
        with st.chat_message("assistant"):
            st.write(message["content"])

# Use a form to allow submitting on Enter
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Your message:")
    submitted = st.form_submit_button("Send")
    if submitted and user_input:
        response = bot.get_response(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()
