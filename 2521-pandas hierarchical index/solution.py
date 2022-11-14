# coding: utf-8
from pandas import DataFrame, Series


def layers_index(data: DataFrame) -> Series:
    """
    :param data: the source data
    :return: return a Series
    """
    # -- write your code here --
    return data.loc['second', 'Ma']['A']
