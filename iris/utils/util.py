import cv2
import numpy as np



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


def extractPupil(img):
    # img = cv2.GaussianBlur(img, ksize=(3, 3), sigmaX=0)
    threshold = np.max(img)/5
    _, binary_image = cv2.threshold(img, threshold, 255, cv2.THRESH_BINARY_INV)
    res = cv2.medianBlur(binary_image, ksize=7)
    return res
