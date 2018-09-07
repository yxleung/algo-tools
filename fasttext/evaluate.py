# -*- coding: utf-8 -*-

import argparse
import fastText as ft
from sklearn.metrics import *


def get_y_pred(model, content):
    clsf = ft.load_model(model)
    result = []
    for line in content:
        tags, probs = clsf.predict(line);
        result.append(tags[0].split('__label__')[1])
    return result


def split_test_set(test_set):
    content = []
    labels = []
    with open(test_set, encoding='utf-8') as f:
        for line in f:
            tmp = line.split('__label__')
            content.append(tmp[0].strip())
            labels.append(tmp[1][:-1])
    return content, labels


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Evaluate fastText model')
    parser.add_argument('model', help='Path to fastText trained model.',
                        default='D:\\NLP\\fasttext_demo\\model\\news_model.ftz')
    parser.add_argument('test_set', help='Path to test set.',
                        default='D:\\NLP\\fasttext_demo\\dataset\\news_fasttext_test.txt')

    args = parser.parse_args()

    content, y_true = split_test_set(args.test_set)
    y_pred = get_y_pred(args.model, content)

    # eq = y_true == y_pred
    # print("Accuracy: " + str(eq.sum() / len(y_true)))
    print("混淆矩阵: ", confusion_matrix(y_true, y_pred))
    print("accuracy: ", accuracy_score(y_true, y_pred))
    # print("f1_score: ", f1_score())
    # print("precision_recall_fscore: ", precision_recall_fscore_support(y_true, y_pred))
    # print(precision_recall_curve(y_true,y_pred))
    print(classification_report(y_true, y_pred))
