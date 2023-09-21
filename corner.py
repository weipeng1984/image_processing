# The following function aims at Detecting Corners
# using the Harris corner detector from OpenCV.


import os
import glob
import cv2 as cv
from pathlib import Path
import numpy as np


def corner(input_directory, block_size, aperture, free_parameter, threshold, output_directory):

    # directory_path = '/Users/weipeng/Downloads/'
    picture_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp']
    picture_files = []
    # Iterate through the specified extensions and search for matching files
    for ext in picture_extensions:
        pattern = os.path.join(input_directory, ext)
        picture_files.extend(glob.glob(pattern))

    for filename in picture_files:
        
        if aperture % 2 == 0:
            print("Error: The aperture should be odd.")
            aperture = aperture + 1
            print(f"Note: The aperture is now automatically adjusted to {aperture}.")
        image_bgr = cv.imread(filename)  # Read the image
        image_gray = cv.cvtColor(image_bgr, cv.COLOR_BGR2GRAY)
        image_gray = np.float32(image_gray)

        # Detect corners
        detector_responses = cv.cornerHarris(image_gray,
                                             block_size,
                                             aperture,
                                             free_parameter)
        # Large corner markers
        detector_responses = cv.dilate(detector_responses, None)
        # Only keep detector responses greater than threshold, mark as white
        image_bgr[detector_responses > threshold *
                  detector_responses.max()] = [255, 255, 255]
        # Convert to grayscale
        corner_img = cv.cvtColor(image_bgr, cv.COLOR_BGR2GRAY)

        # Extract the filename (without path) and file extension
        file_name = os.path.basename(filename)
        file_base_name, file_extension = os.path.splitext(file_name)

        # Define the output filename with "_corner" added
        output_filename = f"{file_base_name}_corner{file_extension}"
        # Define the path to save the preprocessed image
        output_path = os.path.join(output_directory, output_filename)
        # Save the preprocessed image
        cv.imwrite(output_path, corner_img)


# Example usage:
input_directory = '/Users/weipeng/Downloads/'
output_directory = '/Users/weipeng/Downloads/'


corner(input_directory, 3, 20, 0.04, 0.02, output_directory)



