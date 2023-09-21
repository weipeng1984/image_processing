# Just pass the shape and size of the kernel, will get the desired kernel.


import os
import glob
import cv2 as cv
from pathlib import Path
import numpy as np
from matplotlib import pyplot as plt
import pandas as pd

# Rectangular Kernel
cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
# array([[1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1]], dtype=uint8)
# Elliptical Kernel
cv.getStructuringElement(cv.MORPH_ELLIPSE, (5, 5))
# array([[0, 0, 1, 0, 0],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [1, 1, 1, 1, 1],
#        [0, 0, 1, 0, 0]], dtype=uint8)
# Cross-shaped Kernel
cv.getStructuringElement(cv.MORPH_CROSS, (5, 5))
# array([[0, 0, 1, 0, 0],
#        [0, 0, 1, 0, 0],
#        [1, 1, 1, 1, 1],
#        [0, 0, 1, 0, 0],
#        [0, 0, 1, 0, 0]], dtype=uint8)
