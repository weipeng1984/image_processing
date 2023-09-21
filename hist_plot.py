# The following function aims at plotting the intensity
# distribution of an image.


import os
import glob
import cv2 as cv
from pathlib import Path
import numpy as np
from matplotlib import pyplot as plt


def hist_plot(input_directory, output_directory):
    
    # directory_path = '/Users/weipeng/Downloads/'
    picture_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp']
    picture_files = []
    # Iterate through the specified extensions and search for matching files
    for ext in picture_extensions:
        pattern = os.path.join(input_directory, ext)
        picture_files.extend(glob.glob(pattern))

    for filename in picture_files:
        img = cv.imread(filename)
        hist = cv.calcHist([img], [0], None, [256], [0, 256])
        color = ('b', 'g', 'r')
        for i, col in enumerate(color):
            histr = cv.calcHist([img], [i], None, [256], [0, 256])
            plt.plot(histr, color=col)
            plt.xlim([0, 256])
        # Save the histogram plot as an image
        file_name = os.path.basename(filename)
        file_base_name, file_extension = os.path.splitext(file_name)
        output_filename = f"{file_base_name}_hist{file_extension}.png"
        output_path = os.path.join(output_directory, output_filename)
        plt.savefig(output_path)
        plt.close()


# Example usage:
input_directory = '/Users/weipeng/Downloads/'
output_directory = '/Users/weipeng/Downloads/'

hist_plot(input_directory, output_directory)
