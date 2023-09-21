# The following function aims at changing color saturation.
# That is, to change the content of a specific channel in
# the RGB color scheme.
# A factor greater than 1 will increase saturation,
# and a factor less than 1 will decrease it.

import os
import glob
import cv2 as cv
from pathlib import Path
import numpy as np


def saturating(input_directory, saturation_factor, output_directory):

    # directory_path = '/Users/weipeng/Downloads/'
    picture_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp']
    picture_files = []
    # Iterate through the specified extensions and search for matching files
    for ext in picture_extensions:
        pattern = os.path.join(input_directory, ext)
        picture_files.extend(glob.glob(pattern))

    for filename in picture_files:
        img = cv.imread(filename)  # Read the image
        # Convert the image from BGR to HSV color space
        hsv_img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
        # Modify the saturation channel by multiplying it by the saturation factor
        hsv_img[:, :, 1] = np.clip(
            hsv_img[:, :, 1] * saturation_factor, 0, 255)
        # Convert the image back to BGR color space
        saturated_img = cv.cvtColor(hsv_img, cv.COLOR_HSV2BGR)
        # Extract the filename (without path) and file extension
        file_name = os.path.basename(filename)
        file_base_name, file_extension = os.path.splitext(file_name)
        # Define the output filename with "_saturated" added
        output_filename = f"{file_base_name}_saturated{file_extension}"
        # Define the path to save the preprocessed image
        output_path = os.path.join(output_directory, output_filename)
        # Save the preprocessed image
        cv.imwrite(output_path, saturated_img)


# Example usage:
input_directory = '/Users/weipeng/Downloads/'
output_directory = '/Users/weipeng/Downloads/'


saturating(input_directory, 0.6, output_directory)
