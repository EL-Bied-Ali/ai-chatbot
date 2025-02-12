# AI Chatbot Project

This repository contains an intent-based chatbot built with Python, spaCy, and Flask (coming soon). 

## Project Structure

ai-chatbot/ │── data/ │ └── intents.json
│── models/
│── src/ │ ├── chatbot.py
│ └── preprocess.py
│── app.py │── requirements.txt │── .gitignore │── README.md


## Quick Start

1. **Install** dependencies in your Conda environment:
conda activate chatbot-env pip install -r requirements.txt python -m spacy download en_core_web_sm

2. **Run** the basic chatbot from CLI:
python src/chatbot.py

- Type messages, and to exit, type `exit` or `quit`.
3. **Future**: We'll create a Flask (or Streamlit) UI in `app.py`.
Save & close.