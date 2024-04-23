import nltk

class TextProcessor:
    def __init__(self):
        # nltk tokenizer, 불용어 사전 등 초기화
        self.sent_tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
        self.word_tokenizer = nltk.word_tokenize
        self.stopwords = nltk.corpus.stopwords.words('english')

    def preprocess(self, text):
        # 텍스트 전처리 (토큰화, 불용어 제거, 어간 추출 등)
        sentences = self.sent_tokenizer.tokenize(text)
        processed_sentences = []
        for sentence in sentences:
            words = self.word_tokenizer(sentence)
            words = [word.lower() for word in words if word.isalnum() and word not in self.stopwords]
            # ... (어간 추출 등 추가 전처리 작업)
            processed_sentences.append(words)
        return processed_sentences