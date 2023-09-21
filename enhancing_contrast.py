# The following function aims at enhancing contrast.
# Histogram equalization is a tool for image
# processing that can make objects and shapes stand
# out.

import os
import glob
import cv2 as cv
from pathlib import Path
import numpy as np


def enhancing_contrast(input_directory, output_directory):

    # directory_path = '/Users/weipeng/Downloads/'
    picture_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp']
    picture_files = []
    # Iterate through the specified extensions and search for matching files
    for ext in picture_extensions:
        pattern = os.path.join(input_directory, ext)
        picture_files.extend(glob.glob(pattern))

    for filename in picture_files:
        img = cv.imread(filename)  # Read the image
        # Convert to YUV
        img_yuv = cv.cvtColor(img, cv.COLOR_BGR2YUV)
        # Apply histogram equalization
        img_yuv[:, :, 0] = cv.equalizeHist(img_yuv[:, :, 0])
        # Convert to RGB
        enhanced_img = cv.cvtColor(img_yuv, cv.COLOR_YUV2RGB)

        # Extract the filename (without path) and file extension
        file_name = os.path.basename(filename)
        file_base_name, file_extension = os.path.splitext(file_name)

        # Define the output filename with "_enhanced" added
        output_filename = f"{file_base_name}_enhanced{file_extension}"

        # Define the path to save the preprocessed image
        output_path = os.path.join(output_directory, output_filename)

        # Save the preprocessed image
        cv.imwrite(output_path, enhanced_img)


# Example usage:
input_directory = '/Users/weipeng/Downloads/'
output_directory = '/Users/weipeng/Downloads/'

enhancing_contrast(input_directory, output_directory)
