# The following function aims at finding Image gradients, edges etc.
# OpenCV provides three types of gradient filters or High-pass
# filters, Sobel, Scharr and Laplacian.

import os
import glob
import cv2 as cv
from pathlib import Path
import numpy as np


def gradient(input_directory, kernel, output_directory):

    # directory_path = '/Users/weipeng/Downloads/'
    picture_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp']
    picture_files = []
    # Iterate through the specified extensions and search for matching files
    for ext in picture_extensions:
        pattern = os.path.join(input_directory, ext)
        picture_files.extend(glob.glob(pattern))

    for filename in picture_files:
        img = cv.imread(filename, cv.IMREAD_GRAYSCALE)
        laplacian = cv.Laplacian(img, cv.CV_64F)
        sobelx = cv.Sobel(img, cv.CV_64F, 1, 0, ksize=kernel)
        sobely = cv.Sobel(img, cv.CV_64F, 0, 1, ksize=kernel)
        sobel_xy = cv.Sobel(img, cv.CV_64F, 1, 1, ksize=kernel)

        titles = ['Laplacian', 'Sobel X',
                  'Sobel Y', 'Sobel XY']
        gradient_img = [laplacian, sobelx, sobely, sobel_xy]
         # Extract the filename (without path) and file extension
        file_name = os.path.basename(filename)
        file_base_name, file_extension = os.path.splitext(file_name)

        for i, gradient_image in enumerate(gradient_img):
            # Define the output filename with "file_base_name" added
            # Add index to distinguish multiple preprocessed images
            title = titles[i]
            # Define the output filename with "file_base_name" and title added
            output_filename = f"{file_base_name}_{title}{file_extension}"
            # Define the path to save the preprocessed image
            output_path = os.path.join(output_directory, output_filename)
            # Save the preprocessed image
            cv.imwrite(output_path, gradient_image)


# Example usage:
input_directory = '/Users/weipeng/Downloads/'
output_directory = '/Users/weipeng/Downloads/'

gradient(input_directory, 5, output_directory)




