#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
from numpy import ndarray

def create_metrix() -> np.ndarray:
    """
        :return: Return an 8x8 chess board matrix
        """
    # -- write your code here --
    board = [[0 if (x + y) % 2 == 0 else 1 for x in range(8)] for y in range(8)]
    return np.array(board)
