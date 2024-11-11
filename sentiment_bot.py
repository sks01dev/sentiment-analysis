from textblob import TextBlob
from dataclasses import dataclass

@dataclass
class Mood:
    emoji: str
    sentiment: float

def analyze_sentiment(input_text: str, *, sensitivity: float) -> Mood:
    polarity: float = TextBlob(input_text).sentiment.polarity

    friendly_threshold: float = sensitivity
    hostile_threshold: float = -sensitivity  # Fixed typo

    if polarity >= friendly_threshold:
        return Mood('😊', polarity)
    elif polarity <= hostile_threshold:
        return Mood('😠', polarity)
    else:
        return Mood('😐', polarity)

def sentiment_bot():
    print("Welcome to the Sentiment Analysis Bot!")
    print("Type 'exit' or 'quit' to stop the bot.")
    
    while True:
        user_input: str = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye! 👋")
            break
        
        mood_response: Mood = analyze_sentiment(user_input, sensitivity=0.3)
        print(f"Bot: {mood_response.emoji} (Sentiment Score: {mood_response.sentiment:.2f})")

if __name__ == '__main__':
    sentiment_bot()
