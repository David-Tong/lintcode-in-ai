# coding: utf-8
from numpy import ndarray
from sklearn.linear_model import SGDRegressor

def my_model(input_data: ndarray, input_label: ndarray, test_data: ndarray) -> ndarray:
    """
    :param input_data: Input train data which data type is ndarray
    :param input_label: Input label which data type is ndarray
    :param test_data: Input test data which data type is ndarray
    :return: Predictied label for test data which data type should be ndarray
    """
    # write your code here
    reg = SGDRegressor()
    reg.fit(input_data, input_label)
    return reg.predict(test_data)
