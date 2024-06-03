import nltk
#from . import emotion_types
from nltk.corpus import wordnet
from nltk import word_tokenize, pos_tag
from nltk.tokenize import word_tokenize
from collections import defaultdict
from nltk.sentiment import SentimentIntensityAnalyzer


class EmotionDetector:
    def __init__(self):
        # 감정 분석 모델 초기화 (예: VADER)
        self.analyzer = SentimentIntensityAnalyzer()
        self.stopwords = nltk.corpus.stopwords.words('english')
        self.emotion_type=['fear', 'anger', 'sadness', 'joy', 'acceptance', 'disgust', 'anticipation', 'surprise']
        self.emotion_score={}

    def penn_to_wn(self, tag):
        if tag.startswith('J'):
            return wordnet.ADJ
        if tag.startswith('N'):
            return wordnet.NOUN
        if tag.startswith('R'):
            return wordnet.ADV
        if tag.startswith('V'):
            return wordnet.VERB
        
    def find_emotional_words(self, sentence):
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
        words = word_tokenize(sentence.lower())
        filtered_words=[word for word in words if word.isalpha() and word not in self.stopwords and word in nltk.corpus.words.words()]
        

        emotion_score = defaultdict(int)

        for word in filtered_words:
            for emotion, keywords in self.emotion_dict.items():
                if word in keywords:
                    emotion_score[emotion] += 1
        for emotion in emotion_score.keys():
            emotion_score[emotion]=emotion_score[emotion]/len(filtered_words)
        return emotion_score
    
    def find_path_similarity(self, sentence):
        words = word_tokenize(sentence.lower())
        filtered_words=[word for word in words if word.isalpha() and word not in self.stopwords and word in nltk.corpus.words.words()]
        
        emotion_synsets={}
        for emotion in self.emotion_type: emotion_synsets[emotion]=wordnet.synsets(emotion)
        
        #NLTK 기반 품사 태깅 문장 추출 
        tagged_words = pos_tag(filtered_words)
        
        similarities = defaultdict(list)
        average_similarities=defaultdict(dict)
        max_similarities=defaultdict(dict)
        for word, tag in tagged_words:
            #print(word, tag)
            word_synsets=wordnet.synsets(word, pos=self.penn_to_wn(tag)) #[Synset('happy.a.01'), Synset('felicitous.s.02'), Synset('glad.s.02'), Synset('happy.s.04')]
            #print(word_synsets)
            
            for emotion in self.emotion_type:
                for word_synset in word_synsets:
                    for emotion_synset in emotion_synsets[emotion]:
                        similarity = round(word_synset.wup_similarity(emotion_synset),2)
                        if similarity is not None and similarity>0.7: similarities[emotion].append(similarity)
            average_similarities[word] = {emotion: (round(sum(scores)/len(scores),2) if scores else 0) for emotion, scores in similarities.items()}
            max_similarities[word] = {emotion: (max(scores) if scores else 0) for emotion, scores in similarities.items()}
        
        return average_similarities, max_similarities
        
    def detect_emotion(self, sentence):
        # 여기를 작성해주시면 됩니다.
        # 문장별로 8가지 감정별로 분석을 다 해보고
        # 가장 높은 수치의 감정을 반환하거나
        # Thresholds 이상의 수치가 없으면 None을 반환해주면 됩니다.
        emotion_dictionary=self.find_emotional_words(sentence)
        if len(emotion_dictionary.items())==1: return [key for key in emotion_dictionary.keys()][0]

        average_similarities, max_similarities = self.find_path_similarity(sentence)

        avg_score_dict=[]
        max_score_dict=[]

        for _, score_dict in average_similarities.items():
            avg_score_dict.append([k for k,v in score_dict.items() if max(score_dict.values()) == v])
        avg_fdist = nltk.FreqDist(i[0] for i in avg_score_dict if len(i)!=0)
        for _, score_dict in max_similarities.items():
            max_score_dict.append([k for k,v in score_dict.items() if max(score_dict.values()) == v])
        max_fdist = nltk.FreqDist(i[0] for i in avg_score_dict if len(i)!=0)

        avg_emo=avg_fdist.most_common(1)[0][0]
        max_emo=max_fdist.most_common(1)[0][0]
        if avg_emo==max_emo: return avg_emo
        else: return None

        
if __name__ == "__main__":        
    emotion_detector = EmotionDetector()
    print(emotion_detector.detect_emotion("I felt a chill run down my spine as I walked through the dark alley."))
    print(emotion_detector.detect_emotion("I am absolutely furious with how I was treated at the store."))
    print(emotion_detector.detect_emotion("He was stunned by the unexpected turn of events in the story."))