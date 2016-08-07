#/bin/python
# Find the contours in the input image

import numpy as np
import cv2
import matplotlib.pyplot as plt
import CImage

class Contours(CImage.Image):

    def drawContours( self, threshold, thresholdType=cv2.THRESH_BINARY ):

        print "threshold = " , threshold, "threshold type = ", thresholdType
        # Change to grayscale
        imgGray = cv2.cvtColor( self.image, cv2.COLOR_BGR2GRAY )

        # Create mask
        nMaxVal = 255;
        retVal, imgMask = cv2.threshold( imgGray, threshold, nMaxVal, thresholdType )
        imgMaskCopy = imgMask.copy()

        # find contours
        contours, hierarchy = cv2.findContours( imgMask, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE )

        # draw contours
        cv2.drawContours( self.image, contours, -1, (255, 0, 0), 2 )

        #plot
        plt.subplot(211), plt.imshow( imgMaskCopy, cmap='gray' ), plt.title('Mask')
        plt.subplot(212), plt.imshow( self.image )
        plt.title("Contour over the required region")
        plt.show()

    def __del__(self):
        className = self.__class__.__name__
        print className, "deleted!"
