# coding: utf-8
import matplotlib.pyplot as plt

from numpy import ndarray


def bar_plot(x_1: ndarray, num_1: ndarray, x_2: ndarray, num_2: ndarray):
    """
    :param x_1: Coordinates of starting points on the X-axis for the first group which data type is ndarray
    :param num_1: Coordinates on the Y-axis for the first group which data type is ndarray
    :param x_2: Coordinates of starting points on the X-axis for the second group which data type is ndarray
    :param num_2: Coordinates on the Y-axis for the second group which data type is ndarray
    """
    # write your code here
    plt.bar(x_1, num_1, width=0.4, color="red", label="height")
    plt.bar(x_2, num_2, width=0.4, color="blue", label="weight")
    plt.legend()
