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
    novel_sentences = text_processor.preprocess(novel_text)  # 문장 단위로 분리

    # 등장인물 분석
    character_analyzer = emotion_analyizer.CharacterAnalyzer(novel_sentences)
    characters = text_processor.extract_characters()

    # 감정 분석 및 캐릭터 매칭
    emotion_detector = emotion_analyizer.EmotionDetector()
    for sentence in novel_sentences:
        # 감정 분석
        emotion = emotion_detector.detect_emotion(sentence)  # 문장 단위 감정 분석

        # 감정이 존재하면 등장인물과 연결
        if emotion:
            for character in characters:
                if character in sentence:
                    character_analyzer.update_character_emotion(character, emotion)

    # 결과를 TSV 파일로 저장
    character_emotions = character_analyzer.get_character_emotions()
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write("Character\tEmotions\n")
        for character_name, emotions in character_emotions.items():
            file.write(f"{character_name}\t{','.join(emotions)}\n")

    print(f"결과가 {filepath}에 저장되었습니다.")

if __name__ == "__main__":
    main()