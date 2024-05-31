import nltk
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
        fullname = name.split()
        self.first_name = fullname[0]       if len(fullname > 0) else None
        self.middle_name = fullname[1:-1]   if len(fullname > 2) else None
        self.last_name = fullname[-1]       if len(fullname > 1) else None
    
    def __add__(self, other):
        if not isinstance(other, Character):
            return NotImplemented
        
        new_name = ' '.join(filter(None, [
            self.first_name or other.first_name,
            ' '.join(self.middle_name or other.middle_name or []),
            self.last_name or other.last_name
        ]))

        c = Character(new_name)

        for emotion_type, offsets in self.emotions.items():
            c.emotions[emotion_type].extend(offsets)
        for emotion_type, offsets in other.emotions.items():
            c.emotions[emotion_type].extend(offsets)
        
        for emotion_list in c.emotions.values():
            emotion_list.sort()

        return c
    
    def append(self, emotion, offset):
        super().append(emotion, offset)

class CharacterAnalyzer:
    def __init__(self):
        self.characters = []
        self.stop_words = set(stopwords.words('english'))

    def extract_characters(self, sent):
        characters = []
        tokens = word_tokenize(sent)
        pos_tags = pos_tag(tokens)
        ner_tags = ne_chunk(pos_tags)

        # 1. NE Chunking
        iob_tags = tree2conlltags(ner_tags)
        for i, (token, pos, tag) in enumerate(iob_tags):
            if tag == 'B-PERSON':  # PERSON으로 시작하는 경우
                character = Character()
                character.first_name = token
                characters.append(character)

        # 2. NER
        # fullname = [leaf[0] for subtree in ner_tags.subtress() if subtree.label() == 'PERSON' for leaf in subtree.leaves()]
        # if fullname:
        #     character = Character(' '.join(fullname))
        #     characters.append(character)

        # for subtree in ner_tags.subtrees():
        #     if subtree.label() == 'PERSON':
        #         fullname = []
        #         for leaf in subtree.leaves():
        #             fullname.append(leaf[0])
        #         character = Character(' '.join(fullname))
        #         characters.append(character)
                

        # 3. 이름 사전
        for word in tokens:
            if word.lower() in self.name_corpus:
                character = Character()
                character.first_name = word
                characters.append(character)

        return characters

    def analyze_characters(self, novel_sentences):
        for sentence in novel_sentences:
            words = word_tokenize(sentence)
            for word in words:
                if word.lower() in self.stop_words: continue

                if word.endswith("."):
                    word = word[:-1] 
                if word.endswith(","):
                    word = word[:-1] 

                if word[0].isupper() and (words[words.index(word) + 1][0].isupper() or words[words.index(word) + 1] == "."):
                    character_name = word
                    found = False
                    for character in self.characters:
                        if character.first_name == character_name:
                            found = True
                            break
                    if not found:
                        character = Character()
                        character.first_name = character_name
                        self.characters.append(character)
        return self.characters
    