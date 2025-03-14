def compare_emotion_lists(answer_dict, output_dict):
    emotion_types = ['fear', 'anger', 'sadness', 'joy', 'acceptance', 'disgust', 'anticipation', 'surprise']
    true_positive, false_positive, false_negative = 0, 0, 0

    for emotion_type in emotion_types:
        answer_set = set(answer_dict[emotion_type])
        output_set = set(output_dict[emotion_type])
        
        for offset in answer_set + output_set:
            if offset in answer_set and offset in output_set:
                true_positive += 1
            elif offset in answer_set and offset not in output_set:
                false_positive += 1
            elif offset not in answer_set and offset in output_set:
                false_positive += 1
                
    other = true_positive + false_positive + false_negative
    return true_positive, false_positive, len(answer_dict) + len(output_dict) - other, false_negative

def precision(tp, fp):
    return tp / (tp + fp) or 0

def recall(tp, fn):
    return tp / (tp + fn) or 0

def accuracy(tp, fp, tn, fn):
    return (tp + tn) / (tp + tn + fp + fn) or 0

def f1(tp, fp, tn, fn):
    return 2 * precision(tp, fp) * recall(tp, fn) / (precision(tp, fp) + recall(tp, fn)) or 0