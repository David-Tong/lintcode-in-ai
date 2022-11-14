# coding: utf-8
from numpy import ndarray
from sklearn.linear_model import Ridge
from sklearn.model_selection import cross_val_score


def cross_validation(X: ndarray, y: ndarray) -> ndarray:
    """
    :param X: the source data x_train
    :param y: the source data y_train
    :return: return a ndarray
    """
    # -- write your code here --
    return cross_val_score(Ridge(), X, y, cv=4, scoring='neg_mean_absolute_error')
