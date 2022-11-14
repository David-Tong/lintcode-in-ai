# coding: utf-8
from numpy import ndarray
from sklearn.svm import LinearSVC

def SVM(x_train: ndarray, y_train: ndarray, x_test: ndarray) -> ndarray:
    """
    :param x_train: Input training data which data type is ndarray
    :param y_train: Input training label which data type is ndarray
    :param x_test: Input testing data which data type is ndarray
    :return: The prediction made by SVM model which data type should be ndarray
    """
    # write your code here
    clf = LinearSVC()
    clf.fit(x_train, y_train)
    return clf.predict(x_test)
