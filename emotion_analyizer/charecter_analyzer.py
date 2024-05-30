import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.chunk import conlltags2tree, tree2conlltags
from nltk import pos_tag, ne_chunk
class Character:
    def __init__(self, name):
        self.first_name = name.split()[0] or None
        self.middle_name = name.split()[1] if name.split()[2] else None
        self.last_name = name.split()[2] if self.middle_name else name.split()[1] or None
        self.emotion_list = []
    
    def __add__(self, other):
        c = Character()

        c.first_name = self.first_name or other.first_name
        c.middle_name = self.middle_name or other.middle_name
        c.last_name = self.last_name or other.last_name

        c.emotion_list = self.emotion_list + other.emotion_list
        c.emotion_list.sort()

        c.emotion_list.sort(key=lambda x: x[1])
        return c
    
    def append(self, emotion, offset):
        self.emotion_list.append((emotion, offset))

class CharacterAnalyzer:
    def __init__(self):
        self.characters = []
        self.stop_words = set(stopwords.words('english'))

    def extract_characters(self, sent):
        characters = []
        tokens = word_tokenize(sent)
        pos_tags = pos_tag(tokens)

        # 1. NE Chunking
        tree = ne_chunk(pos_tags)
        iob_tags = tree2conlltags(tree)
        for i, (token, pos, tag) in enumerate(iob_tags):
            if tag == 'B-PERSON':  # PERSON으로 시작하는 경우
                character = Character()
                character.first_name = token
                characters.append(character)

        # 2. NER
        ner_tags = nltk.ne_chunk(pos_tag(word_tokenize(sent)))
        for subtree in ner_tags.subtrees():
            if subtree.label() == 'PERSON':
                for leaf in subtree.leaves():
                    token = leaf[0]
                    character = Character()
                    character.first_name = token
                    characters.append(character)

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
    