# The following function aims at applying blurring images with
# various low pass filters.
# As in one-dimensional signals, images also can be filtered
# with various low-pass filters (LPF), high-pass filters (HPF),
# etc. LPF helps in removing noise, blurring images, etc.
# HPF filters help in finding edges in images.
# 2D Convolution ( Image Filtering )


import os
import glob
import cv2 as cv
from pathlib import Path
import numpy as np


def convolution_2D(input_directory, kernel, output_directory):

    # directory_path = '/Users/weipeng/Downloads/'
    picture_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp']
    picture_files = []
    # Iterate through the specified extensions and search for matching files
    for ext in picture_extensions:
        pattern = os.path.join(input_directory, ext)
        picture_files.extend(glob.glob(pattern))

    for filename in picture_files:
        img = cv.imread(filename)  # Read the image
        kernel_new = np.ones((kernel, kernel), np.float32)/(kernel**2)
        con_img = cv.filter2D(img, -1, kernel_new)
        # Extract the filename (without path) and file extension
        file_name = os.path.basename(filename)
        file_base_name, file_extension = os.path.splitext(file_name)

        # Define the output filename with "_convolution_2D" added
        output_filename = f"{file_base_name}_convolution_2D{file_extension}"

        # Define the path to save the preprocessed image
        output_path = os.path.join(output_directory, output_filename)

        # Save the preprocessed image
        cv.imwrite(output_path, con_img)

# Example usage:
input_directory = '/Users/weipeng/Downloads/'
output_directory = '/Users/weipeng/Downloads/'

convolution_2D(input_directory, 5, output_directory)
