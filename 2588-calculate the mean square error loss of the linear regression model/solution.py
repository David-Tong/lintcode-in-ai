# coding: utf-8
from numpy import ndarray, float64
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def lr_mean_squared(x_train: ndarray, x_test: ndarray, y_train: ndarray, y_test: ndarray) -> float64:
    """
    :param x_train: the source data training set feature values
    :param x_test: the source data test set feature values
    :param y_train: the source data training set target value
    :param y_test: the source data test set target value
    :return: return a numpy.float64
    """
    # -- write your code here --
    reg = LinearRegression()
    reg.fit(x_train, y_train)
    y_predict = reg.predict(x_test)

    return mean_squared_error(y_test, y_predict)