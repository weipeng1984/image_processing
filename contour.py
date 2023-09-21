# The following function aims at detecting the
# contour of images.


import os
import glob
import cv2 as cv
import numpy as np

def contour(input_directory, output_directory):
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Supported image file extensions
    picture_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp']

    # Iterate through the specified extensions and search for matching files
    for ext in picture_extensions:
        pattern = os.path.join(input_directory, ext)
        picture_files = glob.glob(pattern)

        for filename in picture_files:
            # Read the image
            img = cv.imread(filename)
            
            # Convert the image to grayscale
            gray_image = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            
            # Detect contours in the grayscale image
            contours, _ = cv.findContours(gray_image, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
            
            # Create an all-white image as a mask
            mask = np.ones_like(gray_image) * 255
            
            # Draw the contours on the mask in black
            cv.drawContours(mask, contours, -1, (0, 0, 0), thickness=cv.FILLED)
            
            # Bitwise-AND the mask with the original image to get the result
            result = cv.bitwise_and(img, img, mask=mask)
            
            # Extract the filename (without path) and file extension
            file_name = os.path.basename(filename)
            file_base_name, file_extension = os.path.splitext(file_name)

            # Define the output filename with "_contours" added
            output_filename = f"{file_base_name}_contours{file_extension}"

            # Define the path to save the image with contours
            output_path = os.path.join(output_directory, output_filename)

            # Save the image with contours
            cv.imwrite(output_path, result)



# Example usage:
input_directory = '/Users/weipeng/Downloads/'
output_directory = '/Users/weipeng/Downloads/'

contour(input_directory, output_directory)
