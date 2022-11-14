# coding: utf-8
from pandas import DataFrame
from numpy import ndarray

from sklearn.cluster import KMeans

def clusting(input_data: DataFrame, random_seed=0) -> ndarray:
    """
    In this function you need to initialize the KNN classifier from sklearn
    :param input_data: Input data which data type is DataFrame
    :return: Data after dimensionality reduction which data type should be ndarray
    """
    # write your code here
    kmeans = KMeans(n_clusters=3, random_state=random_seed)
    kmeans.fit(input_data["X"])
    return kmeans.labels_