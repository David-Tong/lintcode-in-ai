# coding: utf-8
from numpy import ndarray
from sklearn.metrics import precision_score

def precision(true_label: ndarray, pred_label: ndarray) -> float:
    """
    :param true_label: Input true label which data type is ndarray
    :param true_label: Input predictied label which data type is ndarray
    :return: Calculated precision score which data type should be float
    """
    # write your code here
    return precision_score(true_label, pred_label)