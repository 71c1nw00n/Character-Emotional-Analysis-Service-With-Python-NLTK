from collections import defaultdict
class Emotion():
    def __init__(self):
        self.emotions = defaultdict(list)

    def append(self, type, offset):
        if type in ['fear', 'anger', 'sadness', 'joy', 'acceptance', 'disgust', 'anticipation', 'surprise']:
            self.emotions[type].append(offset)
        else: raise ValueError(f"Emotion type '{type}' is not recognized")