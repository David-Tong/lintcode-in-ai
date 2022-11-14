#!/usr/bin/python
# -*- coding: UTF-8 -*-
from numpy import ndarray
import numpy as np

def z_score(data: ndarray) -> ndarray:
    """
    :param featurn: A set of characteristics of the sample set
    :return: Return the dataset after standardization
    """
    # -- write your code here --
    return (data - np.mean(data)) / np.std(data)