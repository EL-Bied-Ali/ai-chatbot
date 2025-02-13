import streamlit as st
from src.chatbot import SimpleChatbot  # Ensure this path is correct

# Initialize chatbot (No longer needs intents.json)
bot = SimpleChatbot()

st.title("💬 AI Chatbot - Enhanced")
st.write("A simple AI-powered chatbot with a built-in chat UI. Press Enter to send your message!")

# Add disclaimer about AI chatbot capabilities
st.info(
    "🔹 This chatbot is powered by a pre-trained AI model from Hugging Face (BlenderBot). "
    "It generates responses dynamically and can handle general conversation. "
    "For advanced AI chatbots, I can integrate ChatGPT API or fine-tune custom models."
)

# Initialize chat history in session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Clear Chat History button
if st.button("Clear Chat History"):
    st.session_state.messages = []
    st.rerun()

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        with st.chat_message("user"):
            st.write(message["content"])
    else:
        with st.chat_message("assistant"):
            st.write(message["content"])

# Chat input form
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("Your message:")
    submitted = st.form_submit_button("Send")
    
    if submitted and user_input:
        response = bot.get_response(user_input)
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.messages.append({"role": "assistant", "content": response})
        st.rerun()
