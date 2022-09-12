# coding: utf-8
from numpy import ndarray
from sklearn.ensemble import RandomForestClassifier


class RandomForest(object):
    def __init__(self, random_seed=0) -> None:
        """
        In this function you need to initialize the Random Forest Classifier from sklearn
        :param random_seed: Given random seed for RandomForestClassifier
        """
        # write your code here
        self.model = RandomForestClassifier(random_state=random_seed)

    def fit_data(self, x_train: ndarray, y_train: ndarray) -> None:
        """
        In this function you need to fit the input data and label to the KNN classifier
        :param x_train: Input data which format is ndarray
        :param y_train: Input label which format is ndarray
        """
        # write your code here
        self.model.fit(x_train, y_train)

    def predict_data(self, x_test: ndarray) -> ndarray:
        """
        In this function you need to use KNN classifier to predict input test data
        :param x_test: Input test data which format is ndarray
        :return: The predicted label for input test data which format is ndarray
        """
        # write your code here
        return self.model.predict(x_test)
