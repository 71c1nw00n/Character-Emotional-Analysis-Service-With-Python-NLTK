from emotion_analyzer import TextProcessor, EmotionDetector, CharacterAnalyzer

def main():
    # 사용자 입력 처리
    novel_text = input("소설 텍스트를 입력하세요: ")

    # 텍스트 전처리
    text_processor = TextProcessor()
    processed_text = text_processor.preprocess(novel_text)

    # 감정 분석
    emotion_detector = EmotionDetector()
    emotions = emotion_detector.detect_emotions(processed_text)

    # 등장인물 분석 및 감정 매칭
    character_analyzer = CharacterAnalyzer()
    character_emotions = character_analyzer.analyze_characters(processed_text, emotions)

    # 결과 출력
    for character_name, emotions in character_emotions.items():
        print(f"{character_name}: {emotions}")

if __name__ == "__main__":
    main()