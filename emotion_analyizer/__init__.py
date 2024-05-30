from .charecter_analyzer import CharacterAnalyzer
from .emotion_detector import EmotionDetector
from .text_processor import TextProcessor

from enum import Enum
class Emotion(Enum):
    FEAR = "fear"
    ANGER = "anger"
    SADNESS = "sadness"
    JOY = "joy"
    ACCEPTANCE = "acceptance"
    DISGUST = "disgust"
    ANTICIPATION = "anticipation"
    SURPRISE = "surprise"