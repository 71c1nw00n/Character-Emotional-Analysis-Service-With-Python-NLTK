# Character Emotional Analysis Service With Python NLTK

## Project Introduction

**Emotion Analyzer** is a program designed to identify character names in a novel text and track the emotional changes of each character over time. The program uses Plutchik's (1980) "Wheel of Emotions" to classify emotions. The extracted emotional information is saved in a TSV file for each character.

## Features

- Identify character names in novel text
- Emotion analysis using Plutchik's Wheel of Emotions
- Track emotional changes of characters over time
- Save emotional changes in a TSV file

## Installation

### 1. Clone the repository and navigate to the directory

```bash
git clone https://github.com/yourusername/emotion-analyzer.git
cd emotion-analyzer
```

### 2. Set up a virtual environment and install required packages

```bash
python -m venv venv
source venv/bin/activate   # On Windows, use venv\Scripts\activate
pip install -r requirements.txt
```

## Usage

### 1. Run the program
```bash
python main.py
```

### 2. Input Example

- Enter your User ID.
- Enter the novel title.
- Enter the novel text.

### 3. Output Example

The program will save the results in a output/<User ID>/<novel title>_<date>.tsv file.


## File Structure

```bash
emotion_analyzer/
    ├── __init__.py                # Module initialization file
    ├── character_analyzer.py      # Character analysis module
    ├── emotion_detector.py        # Emotion detection module
    ├── emotion_types.py           # Emotion types definition file
    ├── text_processor.py          # Text processing module
tests/
    ├── __init__.py                # Module initialization file
    ├── manual_test.py             # Test system output with golden standard
    ├── openai_api_test.py         # Test system output with silver standard
    ├── test_utils.py              # Test each function's precision and recall
LICENSE
README.md
main.py
```


## Contribution
Contributions are welcome! To contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch (git checkout -b feature/new-feature).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature/new-feature).
5. Create a new Pull Request.

## Further Development
Furthermore, if this project is deployed on a web server, it can provide real-time novel analysis for authors, enhancing their productivity.

## License
This project is licensed under the MIT License. See the LICENSE file for details.