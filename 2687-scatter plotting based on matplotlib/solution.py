# coding: utf-8
import matplotlib.pyplot as plt

from numpy import ndarray


def scatter_plot(x_1: ndarray, y_1: ndarray, x_2: ndarray, y_2: ndarray):
    """
    :param x_1: Coordinates on the X-axis for the first group which data type is ndarray
    :param y_1: Coordinates on the Y-axis for the first group which data type is ndarray
    :param x_2: Coordinates on the X-axis for the second group which data type is ndarray
    :param y_2: Coordinates on the Y-axis for the second group which data type is ndarray
    """
    # write your code here
    plt.scatter(x_1, y_1, color="red", marker="o")
    plt.scatter(x_2, y_2, color="blue", marker="*")
