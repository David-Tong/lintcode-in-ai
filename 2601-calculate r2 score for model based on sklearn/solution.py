# coding: utf-8
from numpy import ndarray
from sklearn.metrics import r2_score

def r_square(true_value: ndarray, pred_value: ndarray) -> float:
    """
    :param true_value: True value which data type is ndarray
    :param pred_value: Predictied value which data type is ndarray
    :return: Calculated r2 score which data type should be float
    """
    # write your code here
    return r2_score(true_value, pred_value)
