# The following function aims at fliping images
# both horizontally and vertically.

import os
import glob
import cv2 as cv
from pathlib import Path
import numpy as np


def flipping(input_directory, flip_direction, output_directory):
    # directory_path = '/Users/weipeng/Downloads/'
    picture_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp']
    picture_files = []
    # Iterate through the specified extensions and search for matching files
    for ext in picture_extensions:
        pattern = os.path.join(input_directory, ext)
        picture_files.extend(glob.glob(pattern))

    for filename in picture_files:
        if flip_direction == "horizontal":
            img = cv.imread(filename)  # Read the image
            # Flip the image left-right (horizontally)
            flipped_img = cv.flip(img, 1)
            # Extract the filename (without path) and file extension
            file_name = os.path.basename(filename)
            file_base_name, file_extension = os.path.splitext(file_name)

            # Define the output filename with "_flipped" added
            output_filename = f"{file_base_name}_flipped{file_extension}"

            # Define the path to save the preprocessed image
            output_path = os.path.join(output_directory, output_filename)

            # Save the preprocessed image
            cv.imwrite(output_path, flipped_img)

        elif flip_direction == "vertical":
            img = cv.imread(filename)  # Read the image
            # Flip the image top-down (vertically)
            flipped_img = cv.flip(img, 0)
            # Extract the filename (without path) and file extension
            file_name = os.path.basename(filename)
            file_base_name, file_extension = os.path.splitext(file_name)

            # Define the output filename with "_flipped" added
            output_filename = f"{file_base_name}_flipped{file_extension}"

            # Define the path to save the preprocessed image
            output_path = os.path.join(output_directory, output_filename)
            # Save the preprocessed image
            cv.imwrite(output_path, flipped_img)


# Example usage:

input_directory = '/Users/weipeng/Downloads/'
output_directory = '/Users/weipeng/Downloads/'

flipping(input_directory, "vertical", output_directory)
