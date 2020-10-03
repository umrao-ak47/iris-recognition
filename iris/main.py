import cv2
import numpy as np
from utils import read_data
import settings


data = read_data(settings.DATA_FOLDER_PATH)
images = data['imgs']
labels = data['labels']
# show a sample image
i = 10
cv2.imshow(labels[i][2], images[i])
cv2.waitKey(0)
cv2.destroyAllWindows()