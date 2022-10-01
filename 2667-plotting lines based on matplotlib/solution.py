# coding: utf-8
from numpy import ndarray

import matplotlib.pyplot as plt

def plotting(x: ndarray, y: ndarray):
    """
    :param x: Coordinates of the point on the X-axis
    :param y: Coordinates of the point on the Y-axis
    """
    # write your code here
    plt.plot(x, y)