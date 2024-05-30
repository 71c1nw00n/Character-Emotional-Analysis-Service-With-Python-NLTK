from .text_processor import TextProcessor
from .emotion_detector import EmotionDetector
from .character_analyzer import CharacterAnalyzer
from enum import Enum

__all__ = ["TextProcessor", "EmotionDetector", "CharacterAnalyzer"]

class Emotion(Enum):
    FEAR = 'fear'
    ANGER = 'anger'
    SADNESS = 'sadness'
    JOY = 'joy'
    ACCEPTANCE = "acceptance"
    DISGUST = "disgust"
    ANTICIPATION = "anticipation"
    SURPRISE = "surprise"