# coding: utf-8
from sklearn.metrics import accuracy_score
from numpy import ndarray


def accuracy(y_true: ndarray, y_pre: ndarray) -> float:
    """
    In this function you need to calculate the f1 score using given ture label and predicted label
    :param y_true: Given true label which format is ndarray
    :param y_pre: Given predicted label which format is ndarray
    :return: The f1 socre for given true label and predicted label
    """
    # write your code here
    return accuracy_score(y_true, y_pre)
