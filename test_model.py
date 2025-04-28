# test_model.py

from model import predict_sentiment

def test_predict_positive():
    """Test that positive sentiment is detected correctly."""
    assert predict_sentiment("I am happy today") == "positive"

def test_predict_negative():
    """Test that negative sentiment is detected correctly."""
    assert predict_sentiment("I feel sad") == "negative"

def test_predict_neutral():
    """Test that neutral sentiment is detected correctly."""
    assert predict_sentiment("The sky is blue") == "neutral"
