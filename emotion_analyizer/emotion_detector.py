import nltk
from nltk.tokenize import word_tokenize
from collections import defaultdict
from nltk.sentiment import SentimentIntensityAnalyzer

class EmotionDetector:
    def __init__(self):
        # 감정 분석 모델 초기화 (예: VADER)
        self.analyzer = SentimentIntensityAnalyzer()
        self.stopwords = nltk.corpus.stopwords.words('english')
        self.emotion_dict = {
        'fear': ['fearful', 'scared', 'afraid', 'terrified', 'worried', 'anxious', 'panic', 'alarmed', 'apprehensive', 'nervous'],
        'anger': ['angry', 'mad', 'furious', 'irate', 'enraged', 'irritated', 'resentful', 'agitated', 'hostile', 'outraged'],
        'sadness': ['sad', 'unhappy', 'sorrowful', 'depressed', 'mournful', 'melancholic', 'heartbroken', 'downcast', 'gloomy', 'despondent'],
        'joy': ['happy', 'joyful', 'delighted', 'elated', 'glad', 'content', 'ecstatic', 'blissful', 'cheerful', 'radiant'],
        'acceptance': ['accepting', 'agreeable', 'approving', 'supportive', 'tolerant', 'open-minded', 'embracing', 'forgiving', 'understanding'],
        'disgust': ['disgusted', 'repulsed', 'revolted', 'nauseated', 'distasteful', 'abhorrent', 'loathsome', 'detestable', 'repugnant', 'offended'],
        'anticipation': ['anticipating', 'expecting', 'hopeful', 'eager', 'excited', 'enthusiastic', 'optimistic', 'zealous', 'intent', 'keen'],
        'surprise': ['surprised', 'astonished', 'amazed', 'shocked', 'stunned', 'startled', 'flabbergasted', 'baffled', 'dumbfounded', 'taken aback']
        }

    def detect_emotion(self, sentence):
        # 여기를 작성해주시면 됩니다.
        # 문장별로 8가지 감정별로 분석을 다 해보고
        # 가장 높은 수치의 감정을 반환하거나
        # Thresholds 이상의 수치가 없으면 None을 반환해주면 됩니다.
        words = word_tokenize(sentence.lower())
        filtered_words=[word for word in words if words not in self.stopwords]
        

        emotion_score = defaultdict(int)

        for word in filtered_words:
            for emotion, keywords in self.emotion_dict.items():
                if word in keywords:
                    emotion_score[emotion] += 1
        for emotion in emotion_score.keys():
            emotion_score[emotion]=emotion_score[emotion]/len(filtered_words)
        print(emotion_score)
        
emotion_detector = EmotionDetector()
sentence = "I am so happy and elated to see you!"
emotion=emotion_detector.detect_emotion("I am so happy and elated to see you!")