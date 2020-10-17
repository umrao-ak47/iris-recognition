import os, sys
import random
import cv2
import numpy as np
from PIL import Image
from collections import defaultdict
from queue import SimpleQueue



class ImageDataReader:
    def __init__(self):
        pass
    
    def read(self, path, gray=True):
        """Read all images in given path and return 
        Images and Labels in a dictionary as a list"""
        path_list = self._readAllFilesPath(path)
        images = defaultdict(lambda: defaultdict(list))
        for p in path_list:
            name_list = str.split(p.path, '\\')
            idnum, side = name_list[-3], name_list[-2]
            img = self._readImageFile(p.path, gray)
            if not img is None:
                images[idnum][side].append(img)
        return images
    
    def readRandomFile(self, path, gray=True):
        """Read random image in given path and return 
        Image and Label as a tuple"""
        path_list = self._readAllFilesPath(path)
        random_index = random.randint(0, len(path_list)-1)
        random_path = path_list[random_index].path
        img = self._readImageFile(random_path, gray)
        name, ext = str.split(os.path.split(random_path)[-1], os.path.extsep)
        if img is None:
            return self.readRandomFile(path, gray)
        return (img, name)
            

    def _readImageFile(self, path, gray=True):
        try:
            img = np.array(Image.open(path).convert('RGB'))
            if gray:
                img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            else:
                img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            return img
        except IOError:
            return None
        except Exception as e:
            print(e)
            return None
        return None
    
    def _readAllFilesPath(self, path):
        queue = SimpleQueue()
        queue.put(path)
        paths = []
        while not queue.empty():
            dir = queue.get()
            for p in os.scandir(dir):
                if os.path.isdir(p):
                    queue.put(p)
                else:
                    paths.append(p)
        return paths


class CameraReader:
    def __init__(self, size):
        self.size = size
    
    def read(self):
        pass



# Testing code
if __name__=="__main__":
    # Test read data function
    curdir = os.path.dirname(__file__)
    pdir = os.path.abspath(os.path.join(curdir, os.path.pardir))
    sys.path.insert(0, pdir)
    import settings
    r = ImageDataReader()
    data = r.read(settings.DATA_FOLDER_PATH)
    print(data.keys())