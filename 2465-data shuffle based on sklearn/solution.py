# coding: utf-8
from sklearn.utils import shuffle
from numpy import ndarray


def data_shuffle(data: list, ran_state: int) -> list:
    """
    In this function you need to shuffle the data using given random state.
    :param data: Input data which type is list.
    :param ran_state: Given random state which type is int.
    :return: Data after shuffle which type should be list
    """
    # write your code here
    return shuffle(data, random_state=ran_state)
