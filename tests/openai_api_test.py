from emotion_analyzer import TextProcessor, EmotionDetector, CharacterAnalyzer
from .test_utils import compare_emotion_lists

def run_gemini_api_test(novel_text):
    # Gemini API를 사용하여 감정 분석 수행
    # ... (구현 필요)
    gemini_results = ...

    # 자체 시스템으로 감정 분석 수행
    # ... (기존 코드 활용)
    my_results = ...

    # 결과 비교 및 유사도 계산
    # ... (구현 필요: compare_emotion_lists 활용)
    similarity_score = ...
    print(f"유사도: {similarity_score:.2f}%")