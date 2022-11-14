#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
from numpy import ndarray

def create_arr() -> ndarray:
    """
    In this function you need to create an array which fit the requirement
    :return: Return an 2 * 3 array
    """
    # -- write your code here --
    return np.arange(1, 7).reshape(2, 3)