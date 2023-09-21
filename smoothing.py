# The following function aims at applying blurring images with
# various low pass filters.
# As in one-dimensional signals, images also can be filtered
# with various low-pass filters (LPF), high-pass filters (HPF),
# etc. LPF helps in removing noise, blurring images, etc.
# HPF filters help in finding edges in images.
# 2D Convolution (Image Filtering)
# Image Blurring (Image Smoothing) methods mainly including Averaging, Gaussian Blurring,
# Median Blurring, Bilateral Filtering.


import os
import glob
import cv2 as cv
from pathlib import Path
import numpy as np


def smoothing(input_directory, method, kernel, output_directory):

    # directory_path = '/Users/weipeng/Downloads/'
    picture_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp']
    picture_files = []
    # Iterate through the specified extensions and search for matching files
    for ext in picture_extensions:
        pattern = os.path.join(input_directory, ext)
        picture_files.extend(glob.glob(pattern))

    for filename in picture_files:
        if method == "average":
            img = cv.imread(filename)  # Read the image
            average_img = cv.blur(img, (kernel, kernel))
            # Extract the filename (without path) and file extension
            file_name = os.path.basename(filename)
            file_base_name, file_extension = os.path.splitext(file_name)

            # Define the output filename with "_average" added
            output_filename = f"{file_base_name}_average{file_extension}"

            # Define the path to save the preprocessed image
            output_path = os.path.join(output_directory, output_filename)

            # Save the preprocessed image
            cv.imwrite(output_path, average_img)
        elif method == "Gaussian":
            if kernel % 2 == 0:
                print("Error: The kernel size should be odd.")
                kernel = kernel + 1
                print(f"Note: The kernel is now automatically adjusted to {kernel}.")
            img = cv.imread(filename)  # Read the image
            Gaussian_img = cv.GaussianBlur(img, (kernel, kernel), 0)
            # Extract the filename (without path) and file extension
            file_name = os.path.basename(filename)
            file_base_name, file_extension = os.path.splitext(file_name)

            # Define the output filename with "_Gaussian" added
            output_filename = f"{file_base_name}_Gaussian{file_extension}"

            # Define the path to save the preprocessed image
            output_path = os.path.join(output_directory, output_filename)

            # Save the preprocessed image
            cv.imwrite(output_path, Gaussian_img)
        elif method == "median":
            img = cv.imread(filename)  # Read the image
            median_img = cv.medianBlur(img, kernel)
            # Extract the filename (without path) and file extension
            file_name = os.path.basename(filename)
            file_base_name, file_extension = os.path.splitext(file_name)

            # Define the output filename with "_median" added
            output_filename = f"{file_base_name}_median{file_extension}"

            # Define the path to save the preprocessed image
            output_path = os.path.join(output_directory, output_filename)

            # Save the preprocessed image
            cv.imwrite(output_path, median_img)
        else: # method ==
            print ("Unsupported method!")


# # Example usage:
input_directory = '/Users/weipeng/Downloads/'
output_directory = '/Users/weipeng/Downloads/'

smoothing(input_directory, "Gaussian", 5, output_directory)


        
