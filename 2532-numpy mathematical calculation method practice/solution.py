#!/usr/bin/python
# -*- coding: UTF-8 -*-
import numpy as np
from numpy import ndarray

def calculate(num1: ndarray, num2: ndarray) -> int:
    """
    In this function you need to calculate the formula with the mathematical calculation provided by numpy
    :param num1:  the first calculation parameter
    :param num1:  the second calculation parameter
    :return: Return calculation result without any intermediate variables
    """
    # -- write your code here --
    return (num1 + num2) * (-1 * num1 / 2)
