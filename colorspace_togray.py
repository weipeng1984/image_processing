# The following function aims at converting images from one color-space to
# another, like BGR ↔ Gray, BGR ↔ HSV, HSV ↔ Gray, HSV ↔ RGB, etc.
# First, select the target picture. Second, detect the color space. Third,
# based on the color space of the original image, select the target method.

import os
import glob
import cv2 as cv
from pathlib import Path
import numpy as np


def color_togray(input_directory, output_directory):
    # directory_path = '/Users/weipeng/Downloads/'
    picture_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp']
    picture_files = []
    # Iterate through the specified extensions and search for matching files
    for ext in picture_extensions:
        pattern = os.path.join(input_directory, ext)
        picture_files.extend(glob.glob(pattern))
    for filename in picture_files:
        img = cv.imread(filename)  # Read the image
        gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Extract the filename (without path) and file extension
        file_name = os.path.basename(filename)
        file_base_name, file_extension = os.path.splitext(file_name)

        # Define the output filename with "_togray" added
        output_filename = f"{file_base_name}_togray{file_extension}"

        # Define the path to save the preprocessed image
        output_path = os.path.join(output_directory, output_filename)

        # Save the preprocessed image
        cv.imwrite(output_path, gray_image)


# Example usage:
input_directory = '/Users/weipeng/Downloads/'
output_directory = '/Users/weipeng/Downloads/'

color_togray(input_directory, output_directory)
