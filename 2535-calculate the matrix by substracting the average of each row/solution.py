#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
from numpy import ndarray

def broadcast_test(arr: ndarray) -> ndarray:
    """
    :param arr:  An array you need to calculate
    :return: The result after the subraction
    """
    # -- write your code here --
    brr = arr.mean(axis=1)
    return np.subtract(arr, brr.reshape(-1, 1))
