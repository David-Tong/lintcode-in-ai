import numpy as np
from numpy import ndarray

def arr_slice(arr: ndarray) -> ndarray:
    """
    In this function you need to extract even numbers from a sequential ordered array
    :param arr: Ordered arrays containing 0 to 9
    :return: Return a sequence containing only even numbers
    """
    # -- write your code here --
    condition = np.mod(arr, 2) == 0
    return np.extract(condition, arr)
