# The following function aims at applying adaptive thresholding.
# Thresholding is the process of setting pixels with 
# intensity greater than some value to be white and less 
# than the value to be black. A more advanced technique is 
# adaptive thresholding, where the threshold value for a 
# pixel is determined by the pixel intensities of its neighbors.
# This can be helpful when lighting conditions change 
# over different regions in an image. 
# A major benefit of thresholding is denoising an 
# image—keeping only the most important elements.


import os
import glob
import cv2 as cv
from pathlib import Path
import numpy as np


def thresholding(input_directory, max_output_value, neighborhood_size, subtract_from_mean, output_directory):

    # directory_path = '/Users/weipeng/Downloads/'
    picture_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp']
    picture_files = []
    # Iterate through the specified extensions and search for matching files
    for ext in picture_extensions:
        pattern = os.path.join(input_directory, ext)
        picture_files.extend(glob.glob(pattern))

    for filename in picture_files:
        if neighborhood_size % 2 == 0:
            print("Error: The aperture should be odd.")
            neighborhood_size = neighborhood_size + 1
            print(f"Note: The neighborhood size is now automatically adjusted to {neighborhood_size}.")
        img = cv.imread(filename, cv.IMREAD_GRAYSCALE)  # Read the image
        # Apply adaptive thresholding
        binarized_img = cv.adaptiveThreshold(img,
                                             max_output_value,
                                             cv.ADAPTIVE_THRESH_GAUSSIAN_C,
                                             cv.THRESH_BINARY,
                                             neighborhood_size,
                                             subtract_from_mean)
        # Extract the filename (without path) and file extension
        file_name = os.path.basename(filename)
        file_base_name, file_extension = os.path.splitext(file_name)

        # Define the output filename with "_binarized" added
        output_filename = f"{file_base_name}_binarized{file_extension}"

        # Define the path to save the preprocessed image
        output_path = os.path.join(output_directory, output_filename)

        # Save the preprocessed image
        cv.imwrite(output_path, binarized_img)


# Example usage:
input_directory = '/Users/weipeng/Downloads/'
output_directory = '/Users/weipeng/Downloads/'

thresholding(input_directory, 255, 99, 10, output_directory)



