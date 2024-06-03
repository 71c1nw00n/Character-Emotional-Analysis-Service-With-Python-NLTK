import os, nltk
from datetime import datetime
from ..test_utils import compare_emotion_lists

def run_manual_test(input_file, output_file):
    # txt 파일에서 입력 및 기대 출력값 읽기
    # ... (구현 필요)
    input_text = ...
    expected_output = ...

    # 자체 시스템으로 감정 분석 수행
    # ... (기존 코드 활용)
    my_results = ...

    # 결과 비교 및 유사도 계산
    # ... (구현 필요: compare_emotion_lists 활용)
    similarity_score = ...
    print(f"유사도: {similarity_score:.2f}%")

if __name__ == "__main__":
    run_manual_test()