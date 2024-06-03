from transformers import pipeline
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.chunk import conlltags2tree, tree2conlltags
from nltk import pos_tag, ne_chunk
from collections import defaultdict

class Sentiment():
    def __init__(self):
        self.emotions = defaultdict(list)

    def append(self, type, offset):
        if type in ['fear', 'anger', 'sadness', 'joy', 'acceptance', 'disgust', 'anticipation', 'surprise']:
            self.emotions[type].append(offset)
        else: raise ValueError(f"Emotion type '{type}' is not recognized")

class Character(Sentiment):
    def __init__(self, name):
        super().__init__()
        self.constructed_name = name
        self.set_name(name)

    def set_name(self, name):
        if isinstance(name, str):
            fullname = name.split()
        elif isinstance(name, list):
            fullname = name
        else:
            raise ValueError(f"Character Name '{fullname}' is not list or str")
        
        self.first_name = fullname[0]               if len(fullname) > 0 else None
        self.middle_name = ' '.join(fullname[1:-1]) if len(fullname) > 2 else None
        self.last_name = fullname[-1]               if len(fullname) > 1 else None
    
    def __add__(self, other):
        if not isinstance(other, Character):
            return NotImplemented
        
        new_name = ' '.join(filter(None, [
            self.first_name or other.first_name,
            self.middle_name or other.middle_name,
            self.last_name or other.last_name
        ]))

        c = Character(new_name)
        for emotion_type, offset in self.emotions.items():
            c.append(emotion_type, offset)

        for emotion_type, offset in other.emotions.items():
            c.append(emotion_type, offset)
        
        c.sort()
        return c
    
    def __str__(self) -> str:
        return ' '.join([self.first_name, self.middle_name, self.last_name])
    
    def append(self, emotion, offset) -> None:
        super().append(emotion, offset)

    def sort(self) -> None:
        for emotion_list in self.emotions.values():
            emotion_list.sort()

class CharacterAnalyzer:
    def __init__(self, novel_sents):
        self.sents = novel_sents
        self.character_list(novel_sents)
        self.stop_words = set(stopwords.words('english'))

    def character_list(self, novel_sents):
        self.characters = []
        for sent in novel_sents:
            self.extract_characters(sent)

    def extract_characters(self, sent):
        tokens = word_tokenize(sent)
        pos_tags = pos_tag(tokens)
        ner_tags = ne_chunk(pos_tags)
        iob_tags = tree2conlltags(ner_tags)

        current_character_tokens = []
        for token, pos, tag in iob_tags:
            if tag == 'B-PERSON':  # PERSON으로 시작하는 경우
                self.token_to_char(current_character_tokens)  # 이전에 저장된 이름이 있으면 처리 # 이름이 연달아 나오는 경우를 커버
                current_character_tokens = [token]
            elif tag == 'I-PERSON':  # PERSON 이름의 일부분인 경우
                current_character_tokens.append(token)
            else:
                self.token_to_char(current_character_tokens)  # 사람이름이 끝난 경우 처리
                current_character_tokens = []

        # 문장 마지막이 이름으로 끝난 경우 잔여 토큰 처리
        self.token_to_char(current_character_tokens)

    def token_to_char(self, name_token):
        if name_token:
            full_name = ' '.join(name_token)
            character = Character(full_name)
            self.characters.append(character)

    def update_character_emotion(self, character, emotion, offset):
        character.append(emotion, offset)

if __name__ == "__main__":
    my_character = Character("park seung monkey D luffy jun")

    print(my_character.constructed_name)
    print(my_character.emotions)
    print(my_character)

    my_character.append('joy', 3)
    print(my_character.emotions)

    my_second = Character("park jun")
    my_second.append('fear', 6)
    merged_character = my_character + my_second

    print(merged_character.emotions)