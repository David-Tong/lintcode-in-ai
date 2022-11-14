#!/usr/bin/python
# -*- coding: UTF-8 -*-
from numpy import ndarray
from sklearn.preprocessing import MinMaxScaler


def min_max(data: ndarray) -> ndarray:
    """
    :featurn: A set of characteristics of the sample set
    :return: Return the dataset after standardization
    """
    # -- write your code here --
    scalar = MinMaxScaler()
    scalar.fit(data)
    return scalar.transform(data)
