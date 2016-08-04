#!/bin/python

import CContours
import cv2

# Read an image
img = CContours.Contours('../images/opencv-logo-black.png')
img.drawContours(20, thresholdType=cv2.THRESH_BINARY_INV)
print "Completed..."

del img
