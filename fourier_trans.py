# The following function aims at building
# Fourier Transform of images.

import os
import glob
import cv2 as cv
from pathlib import Path
import numpy as np


def fourier_trans(input_directory, output_directory, scaling_factor=20):
    # directory_path = '/Users/weipeng/Downloads/'
    picture_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp']
    picture_files = []
    # Iterate through the specified extensions and search for matching files
    for ext in picture_extensions:
        pattern = os.path.join(input_directory, ext)
        picture_files.extend(glob.glob(pattern))

    for filename in picture_files:
        img = cv.imread(filename, cv.IMREAD_GRAYSCALE)
        dft = cv.dft(np.float32(img), flags=cv.DFT_COMPLEX_OUTPUT)
        dft_shift = np.fft.fftshift(dft)
        magnitude_spectrum = scaling_factor * \
            np.log(cv.magnitude(dft_shift[:, :, 0], dft_shift[:, :, 1])).astype(
                np.float32)
        # Extract the filename (without path) and file extension
        file_name = os.path.basename(filename)
        file_base_name, file_extension = os.path.splitext(file_name)

        # Define the output filename with "_Fourier" added
        output_filename = f"{file_base_name}_Fourier{file_extension}"

        # Define the path to save the transformed image
        output_path = os.path.join(output_directory, output_filename)

        # Save the transformed image
        cv.imwrite(output_path, magnitude_spectrum)


# Example usage:
input_directory = '/Users/weipeng/Downloads/'
output_directory = '/Users/weipeng/Downloads/'

fourier_trans(input_directory, output_directory, 20)
