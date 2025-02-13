import os
import streamlit as st
from llama_cpp import Llama

MODEL_PATH = "models/mistral/mistral-7b-instruct-v0.1.Q4_K_M.gguf"

# Check if the model exists, if not, download it
if not os.path.exists(MODEL_PATH):
    st.info("Downloading model, please wait...")
    os.makedirs("models/mistral", exist_ok=True)
    os.system(f"wget -O {MODEL_PATH} https://huggingface.co/TheBloke/Mistral-7B-Instruct-v0.1-GGUF/resolve/main/mistral-7b-instruct-v0.1.Q4_K_M.gguf")

# Load model
llm = Llama(model_path=MODEL_PATH, n_ctx=2048)

st.title("AI Chatbot - Powered by Mistral 7B")
user_input = st.text_input("You:", "")

if user_input:
    response = llm(user_input)["choices"][0]["text"]
    st.write(f"**Bot:** {response}")
