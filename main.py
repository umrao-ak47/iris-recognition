import cv2
import numpy as np
import matplotlib.pyplot as plt
import iris.utils
import iris.utils.contours
from iris.utils import ImageDataReader, ImageViewer
import settings



reader = ImageDataReader()
viewer = ImageViewer()

data = reader.read(settings.DATA_FOLDER_PATH, gray=True)


# choose a sample image
img = data["14"]["left"][4]
viewer.addImage("1-Left", img)




i = iris.utils.extractPupil(img)
viewer.addImage("EyeLid", i)

num_labels, labels_im = cv2.connectedComponents(i)

def imshow_components(labels):
    # Map component labels to hue val
    label_hue = np.uint8(179*labels/np.max(labels))
    blank_ch = 255*np.ones_like(label_hue)
    labeled_img = cv2.merge([label_hue, blank_ch, blank_ch])

    # cvt to BGR for display
    labeled_img = cv2.cvtColor(labeled_img, cv2.COLOR_HSV2BGR)

    # set bg label to black
    labeled_img[label_hue==0] = 0

    viewer.addImage('labeled.png', labeled_img)

imshow_components(labels_im)

viewer.show()
plt.show()