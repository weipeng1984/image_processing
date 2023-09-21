# The following function aims performing Image Segmentation
# using different methods, such as K-means,
# Contour Detection, Otsu Thresholding, Color Masking.


import os
import glob
import cv2 as cv
import numpy as np
from skimage.filters import threshold_otsu


def segmentation(input_directory, output_directory, method, cluster=None, attempt=None, low=None, high=None):
    picture_extensions = ['*.jpg', '*.jpeg', '*.png', '*.bmp']
    picture_files = []
    for ext in picture_extensions:
        pattern = os.path.join(input_directory, ext)
        picture_files.extend(glob.glob(pattern))

    for filename in picture_files:
        if method == "kmeans":
            if cluster is None or attempt is None:
                print("Error: Missing attempt and cluster for K-means method.")
            else:
                img = cv.imread(filename)
                img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
                twoDimage = img.reshape((-1, 3))
                twoDimage = np.float32(twoDimage)
                criteria = (cv.TERM_CRITERIA_EPS +
                            cv.TERM_CRITERIA_MAX_ITER, 10, 1.0)
                ret, label, center = cv.kmeans(
                    twoDimage, cluster, None, criteria, attempt, cv.KMEANS_PP_CENTERS)
                center = np.uint8(center)
                res = center[label.flatten()]
                kmeans_img = res.reshape((img.shape))

                file_name = os.path.basename(filename)
                file_base_name, file_extension = os.path.splitext(file_name)
                # Define the output filename with "_kmeans" added
                output_filename = f"{file_base_name}_kmeans{file_extension}"
                # Define the path to save the preprocessed image
                output_path = os.path.join(output_directory, output_filename)
                # Save the preprocessed image
                cv.imwrite(output_path, kmeans_img)

        elif method == "contour":
            img = cv.imread(filename)
            height, width, channels = img.shape
            img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
            _, thresh = cv.threshold(gray, np.mean(
                gray), 255, cv.THRESH_BINARY_INV)
            edges = cv.dilate(cv.Canny(thresh, 0, 255), None)
            cnt = sorted(cv.findContours(edges, cv.RETR_LIST,
                         cv.CHAIN_APPROX_SIMPLE)[-2], key=cv.contourArea)[-1]
            mask = np.zeros((height, width), dtype=np.uint8)
            masked = cv.drawContours(mask, [cnt], -1, 255, -1)
            dst = cv.bitwise_and(img, img, mask=mask)
            contour_img = cv.cvtColor(dst, cv.COLOR_BGR2RGB)

            file_name = os.path.basename(filename)
            file_base_name, file_extension = os.path.splitext(file_name)
            # Define the output filename with "_contour" added
            output_filename = f"{file_base_name}_contour{file_extension}"
           # Define the path to save the preprocessed image
            output_path = os.path.join(output_directory, output_filename)
            # Save the preprocessed image
            cv.imwrite(output_path, contour_img)

        elif method == "thresholding":
            img = cv.imread(filename)
            img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            img_gray = cv.cvtColor(img, cv.COLOR_RGB2GRAY)
            thresh = threshold_otsu(img_gray)
            img_otsu = img_gray < thresh

            def filter_image(image, mask):
                r = image[:, :, 0] * mask
                g = image[:, :, 1] * mask
                b = image[:, :, 2] * mask
                return np.dstack([r, g, b])
            threshold_img = filter_image(img, img_otsu)

            file_name = os.path.basename(filename)
            file_base_name, file_extension = os.path.splitext(file_name)
            # Define the output filename with "_threshold" added
            output_filename = f"{file_base_name}_threshold{file_extension}"
           # Define the path to save the preprocessed image
            output_path = os.path.join(output_directory, output_filename)
            # Save the preprocessed image
            cv.imwrite(output_path, threshold_img)

        elif method == "masking":
            img = cv.imread(filename)
            img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
            if low is None or high is None:
                print("Error: Missing low and high values for color masking.")
                continue
            mask = cv.inRange(img, np.array(low), np.array(high))
            mask_img = cv.bitwise_and(img, img, mask=mask)

            file_name = os.path.basename(filename)
            file_base_name, file_extension = os.path.splitext(file_name)
            # Define the output filename with "_mask" added
            output_filename = f"{file_base_name}_mask{file_extension}"
           # Define the path to save the preprocessed image
            output_path = os.path.join(output_directory, output_filename)
            # Save the preprocessed image
            cv.imwrite(output_path, mask_img)


# Example usage:
input_directory = '/Users/weipeng/Downloads/'
output_directory = '/Users/weipeng/Downloads/'

# Corrected usage
segmentation(input_directory, output_directory, "masking", low=np.array([0, 0, 0]), high=np.array([215, 51, 51]))
