# -*- coding: utf-8 -*-
"""
Created on Thu May  7 05:27:29 2020

@author: Clinton
"""


import cv2

FrameWidth = 800
FrameHeight = 600

cap = cv2.VideoCapture(1)

while True:
    success, img = cap.read()
    img_captured = cv2.resize(img, (FrameWidth, FrameHeight))
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img_grayresize = cv2.resize(img_gray,(FrameWidth, FrameHeight))
    
    cv2.imshow("Captured Image", img_captured)
    cv2.imshow("Gray Scale Image", img_grayresize)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
