class Character:
    def __init__(self):
        self.first_name = None
        self.middle_name = None
        self.last_name = None
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
        self.stop_words = set(stopwords.words('english'))  # 영어 불용어 집합

    def analyze_characters(self, novel_sentences):
        for sentence in novel_sentences:
            words = word_tokenize(sentence)
            for word in words:
                if word.lower() not in self.stop_words:  # 불용어 제외
                    if word.endswith("."):
                        word = word[:-1]  # 마침표 제거
                    if word.endswith(","):
                        word = word[:-1]  # 쉼표 제거

                    # 이름 추출: 단어가 대문자로 시작하고, 다음 단어가 대문자로 시작하거나 . 이면 이름으로 판단
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