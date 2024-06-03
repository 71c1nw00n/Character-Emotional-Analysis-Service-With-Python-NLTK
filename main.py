import os, nltk
from datetime import datetime
from emotion_analyizer import CharacterAnalyzer, EmotionDetector

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

    # 등장인물 분석
    novel_sentences = nltk.sent_tokenize(novel_text)
    character_analyzer = CharacterAnalyzer(novel_sentences)
    characters = character_analyzer.characters

    # 감정 분석 및 캐릭터 매칭
    emotion_detector = EmotionDetector()
    for offset, sentence in enumerate(novel_sentences):
        emotion = emotion_detector.detect_emotion(sentence[0])

        if emotion:
            character_analyzer.resolve_emotion_coref(characters, emotion, offset)

    # 결과를 TSV 파일로 저장
    with open(filepath, 'w', encoding='utf-8') as file:
        for char_num, character in enumerate(characters, start=1):
            file.write(f"Character{char_num}: {character.constructed_name}\n")
            file.write(f"{character.emotions}\n")

    print(f"결과가 {filepath}에 저장되었습니다.")

if __name__ == "__main__":
    main()