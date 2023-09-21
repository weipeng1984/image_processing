# The following function aims at applying different geometric transformations to images, like translation,
# rotation, affine transformation etc.
# Specifically, this function works at cropping the image.

import os
import glob
import cv2 as cv
from pathlib import Path
import numpy as np


def geo_cropping(input_directory, crop_width, crop_height, output_directory):

    # directory_path = '/Users/weipeng/Downloads/'
    picture_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp']
    picture_files = []
    # Iterate through the specified extensions and search for matching files
    for ext in picture_extensions:
        pattern = os.path.join(input_directory, ext)
        picture_files.extend(glob.glob(pattern))

    for filename in picture_files:
        img = cv.imread(filename)  # Read the image
        # Calculate the dimensions for cropping
        left = (img.shape[1] - crop_width) // 2
        top = (img.shape[0] - crop_height) // 2
        right = left + crop_width
        bottom = top + crop_height
        # Crop the image
        cropped_img = img[top:bottom, left:right]
        # Extract the filename (without path) and file extension
        file_name = os.path.basename(filename)
        file_base_name, file_extension = os.path.splitext(file_name)

        # Define the output filename with "_cropping" added
        output_filename = f"{file_base_name}_cropping{file_extension}"

        # Define the path to save the preprocessed image
        output_path = os.path.join(output_directory, output_filename)

        # Save the preprocessed image
        cv.imwrite(output_path, cropped_img)


# Example usage:
input_directory = '/Users/weipeng/Downloads/'
output_directory = '/Users/weipeng/Downloads/'

geo_cropping(input_directory, 1024, 768, output_directory)
