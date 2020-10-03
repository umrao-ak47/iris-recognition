from settings import *
import cv2
import numpy as np
import queue



"""
Read all images in dataset and return Images and 
Labels in a dictionary as a numpy array
"""
def read_data():
    """
     Internal function : Read and returns all the images path
    """
    def read_directory():
        # store read images path in a list
        res = []
        # store all the folder in a queue to walk the dirs
        folder_queue = queue.SimpleQueue()
        # put dataset folder as first entry to enumerate
        folder_queue.put(DATA_FOLDER_PATH)
        while not folder_queue.empty():
            # scan the directory
            for path in os.scandir(folder_queue.get()):
                # if path is a dir push it to queue to enumerate it latet
                if os.path.isdir(path):
                    folder_queue.put(path)
                # if path is a datset image put the path in list
                elif os.path.isfile(path) and path.path.endswith(".bmp"):
                    res.append(path)  
        return res
        
    # Store all image and labels in a list
    imgs = []
    labels = []
    # read all paths using internal function
    files = read_directory()
    # read path as image and get the labels
    for file in files:
        lis = file.path.split('\\')
        idnum, side, name = lis[-3], lis[-2], lis[-1]
        labels.append((idnum, side, name))
        img = cv2.imread(file.path)
        imgs.append(img)
    # return data as dictionary format
    return {
        'imgs' : np.array(imgs),
        'labels': np.array(labels),
    }



# Testing code
if __name__=="__main__":
    # Test read data function
    data = read_data()
    cv2.imshow("Image", data['imgs'][0])
    print(data['labels'][0])
    cv2.waitKey(0)
    cv2.destroyAllWindows()

