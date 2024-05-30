import os, nltk
from datetime import datetime
import emotion_analyizer

def main():
    # 사용자 입력 처리
    user_id = input("User ID를 입력하세요: ")
    novel_title = input("소설 제목을 입력하세요: ")
    novel_text = input("소설 텍스트를 입력하세요: ")

    # 디렉토리 생성
    user_directory = os.path.join("output", user_id)
    os.makedirs(user_directory, exist_ok=True)

    # 파일명 생성
    current_date = datetime.now().strftime("%Y%m%d")
    filename = f"{novel_title}_{current_date}.tsv"
    filepath = os.path.join(user_directory, filename)
    
    # 텍스트 전처리
    text_processor = emotion_analyizer.TextProcessor()
    processed_text = text_processor.preprocess(novel_text)

    # 감정 분석
    emotion_detector = emotion_analyizer.EmotionDetector()
    emotions = emotion_detector.detect_emotions(processed_text)

    # 등장인물 분석 및 감정 매칭
    characters = text_processor.extract_characters()
    character_analyzer = emotion_analyizer.CharacterAnalyzer(characters)

    for sentence, emotion in zip(processed_text, emotions):
        sentence_text = ' '.join(sentence)
        for character in characters:
            if character in sentence_text:
                character_analyzer.update_character_emotion(character, emotion)

    character_emotions = character_analyzer.get_character_emotions()

    # 결과를 TSV 파일로 저장
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write("Character\tEmotions\n")
        for character_name, emotions in character_emotions.items():
            file.write(f"{character_name}\t{','.join(emotions)}\n")

    print(f"결과가 {filepath}에 저장되었습니다.")

if __name__ == "__main__":
    main()