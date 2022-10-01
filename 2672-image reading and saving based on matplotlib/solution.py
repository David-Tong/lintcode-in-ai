# coding: utf-8
import matplotlib.pyplot as plt


def load_and_save_image(input_dir: str, output_dir: str):
    """
    :param input_dir: The direction of input image, like: '../input/img.png'
    :param output_dir: The direction of output imagae, like: '../output/img.png
    """
    # write your code here
    plt.imread(input_dir)
    plt.savefig(output_dir)