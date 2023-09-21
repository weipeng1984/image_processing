# The following function aims at sharpening images by
# apply the Gaussian smoothing filter to a copy of an
# image and subtract the smoothed version from the original
# image (in a weighted way so that the values of a constant
# area remain constant).
# Sharpening is the process of enhancing the edges and
# fine details in an image to make it appear sharper and more defined.

import os
import glob
import cv2 as cv
from pathlib import Path
import numpy as np


def sharpening(input_directory, method, output_directory, sharpening_kernel=None):

    # directory_path = '/Users/weipeng/Downloads/'
    picture_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp']
    picture_files = []
    # Iterate through the specified extensions and search for matching files
    for ext in picture_extensions:
        pattern = os.path.join(input_directory, ext)
        picture_files.extend(glob.glob(pattern))

    for filename in picture_files:
        if method == "filter2D":
            if sharpening_kernel is None:
                print("Error: Missing sharpening_kernel for filter2D method.")
            else:
                img = cv.imread(filename)  # Read the image
                # Apply the user-defined sharpening kernel
                sharpened_img = cv.filter2D(img, -1, sharpening_kernel)
                # Extract the filename (without path) and file extension
                file_name = os.path.basename(filename)
                file_base_name, file_extension = os.path.splitext(file_name)
                # Define the output filename with "_sharpened" added
                output_filename = f"{file_base_name}_sharpened{file_extension}"

                # Define the path to save the preprocessed image
                output_path = os.path.join(output_directory, output_filename)

                # Save the preprocessed image
                cv.imwrite(output_path, sharpened_img)

        elif method == "Laplacian":
            img = cv.imread(filename)  # Read the image
            # Apply the Laplacian sharpening tool
            sharpened_img = cv.Laplacian(img, cv.CV_64F)
            # Extract the filename (without path) and file extension
            file_name = os.path.basename(filename)
            file_base_name, file_extension = os.path.splitext(file_name)
            # Define the output filename with "_sharpened" added
            output_filename = f"{file_base_name}_sharpened{file_extension}"

            # Define the path to save the preprocessed image
            output_path = os.path.join(output_directory, output_filename)

            # Save the preprocessed image
            cv.imwrite(output_path, sharpened_img)
        else:
            print(f"Error: Unknown sharpening method '{method}'.")


# Example usage:
input_directory = '/Users/weipeng/Downloads/'
output_directory = '/Users/weipeng/Downloads/'
# # Define a sharpening kernel (Laplacian kernel)
# sharpening_kernel = np.array([[-1, -1, -1],
#                               [-1,  9, -1],
#                               [-1, -1, -1]], dtype=np.float32)


sharpening(input_directory, "Laplacian", output_directory)
