# The following function aims at detecting edge in pictures.
# it contains five steps: Noise Reduction, Finding Intensity
# Gradient of the Image, Non-maximum Suppression, Hysteresis Thresholding.


import os
import glob
import cv2 as cv
from pathlib import Path
import numpy as np


def edge(input_directory, output_directory):

    # directory_path = '/Users/weipeng/Downloads/'
    picture_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp']
    picture_files = []
    # Iterate through the specified extensions and search for matching files
    for ext in picture_extensions:
        pattern = os.path.join(input_directory, ext)
        picture_files.extend(glob.glob(pattern))

    for filename in picture_files:
        img = cv.imread(filename, cv.IMREAD_GRAYSCALE)  # Read the image
        # Calculate median intensity
        median_intensity = np.median(img)
        # Set thresholds to be one standard deviation above and below median intensity
        lower_threshold = int(max(0, (1.0 - 0.33) * median_intensity))
        upper_threshold = int(min(255, (1.0 + 0.33) * median_intensity))
        edges_img = cv.Canny(img, lower_threshold, upper_threshold)
        # Extract the filename (without path) and file extension
        file_name = os.path.basename(filename)
        file_base_name, file_extension = os.path.splitext(file_name)

        # Define the output filename with "_edge" added
        output_filename = f"{file_base_name}_edge{file_extension}"

        # Define the path to save the preprocessed image
        output_path = os.path.join(output_directory, output_filename)

        # Save the preprocessed image
        cv.imwrite(output_path, edges_img)


# Example usage:
input_directory = '/Users/weipeng/Downloads/'
output_directory = '/Users/weipeng/Downloads/'

edge(input_directory, output_directory)
