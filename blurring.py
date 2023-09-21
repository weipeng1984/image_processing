# The following function aims at blurring images.

import os
import glob
import cv2 as cv
from pathlib import Path
import numpy as np


def blurring(input_directory, kernel_size, output_directory):
    if kernel_size % 2 == 0:
        print("Error: The kernel size should be odd.")
        return  # Stop the script

    # directory_path = '/Users/weipeng/Downloads/'
    picture_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp']
    picture_files = []
    # Iterate through the specified extensions and search for matching files
    for ext in picture_extensions:
        pattern = os.path.join(input_directory, ext)
        picture_files.extend(glob.glob(pattern))

    for filename in picture_files:
        img = cv.imread(filename)  # Read the image
        # Apply Gaussian blur with the specified kernel size
        blurred_img = cv.GaussianBlur(img, (kernel_size, kernel_size), 0)
        # Extract the filename (without path) and file extension
        file_name = os.path.basename(filename)
        file_base_name, file_extension = os.path.splitext(file_name)

        # Define the output filename with "_blurring" added
        output_filename = f"{file_base_name}_blurring{file_extension}"

        # Define the path to save the preprocessed image
        output_path = os.path.join(output_directory, output_filename)

        # Save the preprocessed image
        cv.imwrite(output_path, blurred_img)

# Example usage:
input_directory = '/Users/weipeng/Downloads/'
output_directory = '/Users/weipeng/Downloads/'

blurring(input_directory, 5, output_directory)


