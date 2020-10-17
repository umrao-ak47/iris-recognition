import cv2
import numpy as np
import matplotlib.pyplot as plt
import utils
import utils.contours
import settings
from utils import ImageDataReader

def extract_eyelid(img):
    smooth_img = img
    for i in range(100):
        smooth_img = cv2.medianBlur(smooth_img, ksize=3)
    edges = cv2.Canny(smooth_img, 50, 100)
    circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, 1, 20,
                param1=50,param2=30,minRadius=0, maxRadius=0)

    return circles


reader = ImageDataReader()
data = reader.read(settings.DATA_FOLDER_PATH)

# choose a sample image
img = data["1"]["left"][0]


