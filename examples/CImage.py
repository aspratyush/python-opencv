#/bin/python
# Abstract image class

import cv2

class Image:

    def __init__(self, path):
        self.path = path
        self.image = cv2.imread(path)

    def __del__(self):
        className = self.__class__.__name__
        print className, "deleted!"
