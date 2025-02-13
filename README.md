# AI Chatbot Demo

A simple AI-powered chatbot built with Streamlit, spaCy, and scikit-learn.

## Project Overview

This chatbot is a proof-of-concept AI assistant that can process user queries, match intents using TF-IDF and cosine similarity, and provide responses with basic memory for follow-up questions. The chatbot is deployed with Streamlit, making it easily accessible through a web-based interface.

## Features

- Interactive Chat UI with Streamlit
- Intent Recognition using TF-IDF and cosine similarity
- Multi-Turn Context Handling for follow-up questions
- Follow-Up Support to recognize queries like "What else?"
- Clear Chat History feature
- Easily Extensible with additional intents and responses

## Live Demo

Try the chatbot here:  
[AI Chatbot (Live)](https://el-bied-ali-ai-chatbot.streamlit.app/)

## Technologies Used

- Python 3.9
- Streamlit for UI and deployment
- spaCy for NLP processing
- scikit-learn for TF-IDF vectorization and cosine similarity
- Git and GitHub for version control

## Project Structure

```
ai-chatbot
├── data
│   ├── intents.json            # Predefined chatbot responses
├── src
│   ├── chatbot.py              # Core chatbot logic
├── app.py                      # Streamlit UI
├── requirements.txt            # Dependencies
├── README.md                   # Project documentation
```

## How to Run Locally

### 1. Clone the Repository
```sh
git clone https://github.com/EL-Bied-Ali/ai-chatbot.git
cd ai-chatbot
```

### 2. Set Up the Virtual Environment

#### If using Conda:
```sh
conda create --name chatbot-env python=3.9 -y
conda activate chatbot-env
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```
#### If using venv:
```sh
python -m venv chatbot-env
source chatbot-env/bin/activate  # On macOS/Linux
chatbot-env\Scripts\activate     # On Windows
pip install -r requirements.txt
python -m spacy download en_core_web_sm
```

### 3. Run the Application
```sh
streamlit run app.py
```
Once the server starts, open your browser and go to `http://localhost:8501/`.

## How It Works

1. User input is processed using spaCy for text preprocessing.
2. The chatbot matches the input with predefined intent patterns using TF-IDF vectorization and cosine similarity.
3. The system selects the closest matching intent and provides a response from `intents.json`.
4. The chatbot maintains memory of past interactions to improve follow-up responses.
5. The Streamlit UI displays the conversation dynamically, allowing for real-time interactions.

## Future Enhancements

This chatbot is designed as a proof-of-concept, but future improvements could include:

- Integration with Hugging Face models for more advanced NLP capabilities
- Advanced context awareness to maintain long-term memory across interactions
- An analytics dashboard to track chatbot usage and user queries
- API integration for real-world applications such as customer support

## License

This project is open-source and available under the MIT License.

## Contact

If you have any questions, want to collaborate, or need a chatbot for your project, feel free to reach out:

- Email: ali.el.bied9898@gmail.com  
- GitHub: [EL-Bied-Ali](https://github.com/EL-Bied-Ali)  
- Upwork Profile [Link](https://www.upwork.com/freelancers/~01e7d0b4cdee8ff16f)
