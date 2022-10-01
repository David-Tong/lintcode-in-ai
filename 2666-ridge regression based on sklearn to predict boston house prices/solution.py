# coding: utf-8
from numpy import ndarray
from sklearn.linear_model import Ridge


def my_model(x_train: ndarray, y_train: ndarray, x_test: ndarray) -> ndarray:
    """
    In this function you need to initialize the Ridge from sklearn
    :param x_train: Input train data which data type is ndarray
    :param y_train: Input label which data type is ndarray
    :param x_test: Input test data which data type is ndarray
    :return: Predictied label for test data which data type should be ndarray
    """
    # write your code here
    clf = Ridge(alpha=1.0)
    clf.fit(x_train, y_train)
    return clf.predict(x_test)
