from nltk.sentiment import SentimentIntensityAnalyzer

class EmotionDetector:
    def __init__(self):
        # 감정 분석 모델 초기화 (예: VADER)
        self.analyzer = SentimentIntensityAnalyzer()

    def detect_emotion(self, sentence):
        for word in sentence.split():
            if word in emotion_types.Emotion:
                return word
        return None  # 감정이 발견되지 않으면 None 반환