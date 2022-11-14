#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
from numpy import ndarray

def create_rgba_dtype() -> ndarray:
    """
    :return: Return an array contain elements of type rgba
    """
    # -- write your code here --
    array = [255, 255, 255, 1]
    rgba = np.dtype([('r', np.ubyte), ('g', np.ubyte), ('b', np.ubyte), ('a', np.ubyte)])
    return np.asarray(a=array, dtype=rgba)