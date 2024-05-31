from nltk.sentiment import SentimentIntensityAnalyzer
from . import emotion_types
class EmotionDetector:
    def __init__(self):
        # 감정 분석 모델 초기화 (예: VADER)
        self.analyzer = SentimentIntensityAnalyzer()

    def detect_emotion(self, sentence):
        # 여기를 작성해주시면 됩니다.
        # 문장별로 8가지 감정별로 분석을 다 해보고
        # 가장 높은 수치의 감정을 반환하거나
        # Thresholds 이상의 수치가 없으면 None을 반환해주면 됩니다.