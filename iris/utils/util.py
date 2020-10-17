import cv2
import numpy as np


"""
Returns an binary image for a GRAYSCALE image using 
calculated threshold value. Taking 5 regions in iris images
"""
def binarize_image(img):
    threshold = np.max(img)/5
    _, binary_image = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY_INV)
    return binary_image

def moving_avg(hist, alpha=0.9):
    ### calculate avg
    avg = 0
    vec = []
    for i in range(len(hist)):
        avg = alpha*avg + (1-alpha)*hist[i]
        vec.append(avg)
    return vec


def window_avg(hist, size=10, alpha=0.9):
    vec = []
    sum = 0
    for i in range(len(hist)):
        if i<size:
            sum += hist[i]
            vec.append(hist[i])
        else:
            avg = alpha*(sum/size) + (1-alpha)*hist[i]
            sum = sum+hist[i]-hist[i-size]
            vec.append(avg)
    return vec