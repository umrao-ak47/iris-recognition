import cv2 
import numpy as np

"""
Returns all contoures list for a given 
GRAYSCALE image
"""
def get_all_contours(img):
    contours, hiercharcy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours

"""
Draws and the contours on provided image
"""
def draw_all_contours(img, contours, color = (0, 255, 0)):
    nimg = img.copy()
    cv2.drawContours(nimg, contours, -1, color, 1)
    return nimg

"""
Returns contour that has the maximum area
"""
def get_biggest_contour(contours_list):
    if len(contours_list) == 0:
        raise "Contours List can't be empty"
    bigContour = contours_list[0]
    max_area = cv2.contourArea(bigContour)
    for i in range(1, len(contours_list)):
        area = cv2.contourArea(contours_list[i])
        if area > max_area:
            max_area = area
            bigContour = contours_list[i]
    return bigContour


"""
Draws biggest contour on the image
"""
def draw_biggest_contour(img, contour, color=(0, 0, 255)):
    x, y, r = find_enclosing_circle(contour)
    nimg = img.copy()
    cv2.circle(nimg, (x,y), r, (0, 0, 255), 1)
    #cv2.drawContours(nimg, [contour], -1, color, 1)
    return nimg


"""
Returns the center and radius of enclosing cicrle
to the contour
"""
def find_enclosing_circle(contour):
    (pupilCenterX, pupilCenterY), pupilRadius = cv2.minEnclosingCircle(contour)
    (pupilCenterX, pupilCenterY)  = (int(pupilCenterX), int(pupilCenterY))
    pupilRadius = int(pupilRadius)

    return (pupilCenterX, pupilCenterY, pupilRadius)