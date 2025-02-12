import streamlit as st
from src.chatbot import SimpleChatbot

# Initialize chatbot
bot = SimpleChatbot("data/intents.json")

# Custom styling for chat bubbles
st.markdown(
    """
    <style>
    .chat-container {
        max-width: 700px;
        margin: auto;
    }
    .user-bubble {
        background-color: #DCF8C6;
        padding: 10px;
        border-radius: 10px;
        max-width: 80%;
        margin-bottom: 5px;
        text-align: left;
    }
    .bot-bubble {
        background-color: #EAEAEA;
        padding: 10px;
        border-radius: 10px;
        max-width: 80%;
        margin-bottom: 5px;
        text-align: left;
    }
    .message {
        display: flex;
        align-items: center;
        margin-bottom: 10px;
    }
    .avatar {
        width: 35px;
        height: 35px;
        border-radius: 50%;
        margin-right: 10px;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.title("💬 AI Chatbot")
st.write("A simple AI-powered chatbot with a modern UI.")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(
            f"<div class='message'><img class='avatar' src='https://cdn-icons-png.flaticon.com/512/847/847969.png'><div class='user-bubble'>{message['content']}</div></div>",
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"<div class='message'><img class='avatar' src='https://cdn-icons-png.flaticon.com/512/4712/4712039.png'><div class='bot-bubble'>{message['content']}</div></div>",
            unsafe_allow_html=True,
        )
st.markdown("</div>", unsafe_allow_html=True)

# User input box
user_input = st.text_input("Type your message here:", "")

if st.button("Send"):
    if user_input:
        response = bot.get_response(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.messages.append({"role": "bot", "content": response})
        st.rerun()
