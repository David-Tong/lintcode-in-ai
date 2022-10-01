# coding: utf-8
import matplotlib.pyplot as plt


def subplot_image(input_dir: str):
    """
    :param input_dir: The direction of input image, like: '../input/img.png'
    """
    # write your code here
    ROWS = 2
    COLUMNS = 2

    image = plt.imread(input_dir)

    for x in range(ROWS * COLUMNS):
        ax = plt.subplot(ROWS, COLUMNS, x + 1)
        ax.set_xticks([])
        ax.set_yticks([])
        ax.imshow(image)