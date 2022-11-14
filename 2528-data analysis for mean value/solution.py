# coding: utf-8
from pandas import DataFrame


def calculate_average(data: DataFrame) -> float:
    """
    :param data: the source data
    :return: return a float
    """
    # -- write your code here --
    return data.loc[:, "IMDB"].mean(axis=0)
