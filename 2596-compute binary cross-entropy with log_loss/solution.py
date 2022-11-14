# coding: utf-8
from numpy import ndarray
from sklearn.metrics import log_loss


def binary_cross_entropy(true_label: ndarray, predicted_label: ndarray) -> float:
    """
    :param true_label: the source data test set target value
    :param predicted_label: the source data predicted set target value
    :return: return a numpy.float64
    """
    # -- write your code here --
    return log_loss(true_label, predicted_label)
