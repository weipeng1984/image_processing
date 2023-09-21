# The following function aims at different morphological operations like
#  Erosion, Dilation, Opening, Closing etc.


import os
import glob
import cv2 as cv
from pathlib import Path
import numpy as np


def morpho_trans(input_directory, method, kernel, iteration, output_directory):

    # directory_path = '/Users/weipeng/Downloads/'
    picture_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp']
    picture_files = []
    # Iterate through the specified extensions and search for matching files
    for ext in picture_extensions:
        pattern = os.path.join(input_directory, ext)
        picture_files.extend(glob.glob(pattern))

    for filename in picture_files:
        if method == "erosion":
            img = cv.imread(filename)
            kernel_new = np.ones((kernel, kernel), np.uint8)
            erosion_img = cv.erode(img, kernel_new, iterations=iteration)
            # Extract the filename (without path) and file extension
            file_name = os.path.basename(filename)
            file_base_name, file_extension = os.path.splitext(file_name)

            # Define the output filename with "_erosion" added
            output_filename = f"{file_base_name}_erosion{file_extension}"

            # Define the path to save the preprocessed image
            output_path = os.path.join(output_directory, output_filename)

            # Save the preprocessed image
            cv.imwrite(output_path, erosion_img)
        elif method == "dilation":
            img = cv.imread(filename)
            kernel = np.ones((kernel, kernel), np.uint8)
            dilation_img = cv.dilate(img, kernel, iterations=iteration)
            # Extract the filename (without path) and file extension
            file_name = os.path.basename(filename)
            file_base_name, file_extension = os.path.splitext(file_name)

            # Define the output filename with "_dilation" added
            output_filename = f"{file_base_name}_dilation{file_extension}"

            # Define the path to save the preprocessed image
            output_path = os.path.join(output_directory, output_filename)

            # Save the preprocessed image
            cv.imwrite(output_path, dilation_img)
        elif method == "opening":
            img = cv.imread(filename)
            kernel_new = np.ones((kernel, kernel), np.uint8)
            opening_img = cv.morphologyEx(img, cv.MORPH_OPEN, kernel_new)
            # Extract the filename (without path) and file extension
            file_name = os.path.basename(filename)
            file_base_name, file_extension = os.path.splitext(file_name)

            # Define the output filename with "_opening" added
            output_filename = f"{file_base_name}_opening{file_extension}"

            # Define the path to save the preprocessed image
            output_path = os.path.join(output_directory, output_filename)

            # Save the preprocessed image
            cv.imwrite(output_path, opening_img)
        elif method == "closing":
            img = cv.imread(filename)
            kernel_new = np.ones((kernel, kernel), np.uint8)
            closing_img = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel_new)
            # Extract the filename (without path) and file extension
            file_name = os.path.basename(filename)
            file_base_name, file_extension = os.path.splitext(file_name)

            # Define the output filename with "_erosion" added
            output_filename = f"{file_base_name}_erosion{file_extension}"

            # Define the path to save the preprocessed image
            output_path = os.path.join(output_directory, output_filename)

            # Save the preprocessed image
            cv.imwrite(output_path, closing_img)
        elif method == "gradient":
            img = cv.imread(filename)
            kernel_new = np.ones((kernel, kernel), np.uint8)
            gradient_img = cv.morphologyEx(img, cv.MORPH_GRADIENT, kernel_new)
            # Extract the filename (without path) and file extension
            file_name = os.path.basename(filename)
            file_base_name, file_extension = os.path.splitext(file_name)

            # Define the output filename with "_gradient" added
            output_filename = f"{file_base_name}_gradient{file_extension}"

            # Define the path to save the preprocessed image
            output_path = os.path.join(output_directory, output_filename)

            # Save the preprocessed image
            cv.imwrite(output_path, gradient_img)
        elif method == "tophat":
            img = cv.imread(filename)
            kernel_new = np.ones((kernel, kernel), np.uint8)
            tophat_img = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel_new)
            # Extract the filename (without path) and file extension
            file_name = os.path.basename(filename)
            file_base_name, file_extension = os.path.splitext(file_name)

            # Define the output filename with "_tophat" added
            output_filename = f"{file_base_name}_tophat{file_extension}"

            # Define the path to save the preprocessed image
            output_path = os.path.join(output_directory, output_filename)

            # Save the preprocessed image
            cv.imwrite(output_path, tophat_img)
        elif method == "blackhat":
            img = cv.imread(filename)
            kernel_new = np.ones((kernel, kernel), np.uint8)
            blackhat_img = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel_new)
            # Extract the filename (without path) and file extension
            file_name = os.path.basename(filename)
            file_base_name, file_extension = os.path.splitext(file_name)

            # Define the output filename with "_blackhat" added
            output_filename = f"{file_base_name}_blackhat{file_extension}"

            # Define the path to save the preprocessed image
            output_path = os.path.join(output_directory, output_filename)

            # Save the preprocessed image
            cv.imwrite(output_path, blackhat_img)
        else:
            print("Unsupported method!")


# Example usage:
input_directory = '/Users/weipeng/Downloads/'
output_directory = '/Users/weipeng/Downloads/'

morpho_trans(input_directory, "closing", 5, 1, output_directory)
