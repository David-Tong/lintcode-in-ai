# coding: utf-8
from pandas import Series
import numpy as np
import pandas as pd


def create_series() -> Series:
    """
    :return: return a Series, def create_series() -> Series:
    """
    sequence = np.arange(0, 4)
    index = ['a', 'b', 'c', 'd']
    series = pd.Series(data=sequence, index=index, name="python")
    return series


print(create_series())
