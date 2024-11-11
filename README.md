
# Sentiment Analysis Bot 🤖

This project is a simple **Sentiment Analysis Bot** built using Python's **TextBlob** library. The bot analyzes the sentiment of user-provided text and responds with an appropriate emoji based on the sentiment score. 

## 🌟 Features
- Analyzes text sentiment in real-time.
- Provides three types of feedback:
  - 😊 (Positive sentiment)
  - 😠 (Negative sentiment)
  - 😐 (Neutral sentiment)
- Adjustable sensitivity for sentiment analysis.
- Simple command-line interface.

## 🛠️ Technologies Used
- **Python 3.x**
- **TextBlob** library for NLP tasks
- **dataclasses** for structured data storage

## 📦 Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/your-username/sentiment-analysis-bot.git
    cd sentiment-analysis-bot
    ```

2. **Create a virtual environment (optional)**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3. **Install the required dependencies**:
    ```bash
    pip install textblob
    ```

## 🚀 How to Run the Bot

```bash
python sentiment_bot.py
```

## 📝 Example Usage

```
Welcome to the Sentiment Analysis Bot!
Type 'exit' or 'quit' to stop the bot.
You: I love programming!
Bot: 😊 (Sentiment Score: 0.50)
You: This is the worst day ever.
Bot: 😠 (Sentiment Score: -0.80)
You: I'm feeling okay.
Bot: 😐 (Sentiment Score: 0.00)
You: exit
Goodbye! 👋
```

## ⚙️ Adjusting Sensitivity
You can adjust the sentiment sensitivity threshold by modifying the `sensitivity` parameter in the code:
```python
mood_response: Mood = analyze_sentiment(user_input, sensitivity=0.5)
```

## 🤝 Contributing
Feel free to submit issues or pull requests if you want to improve the bot!

