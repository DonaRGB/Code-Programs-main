import cv2
import numpy as np
import matplotlib.pyplot as plt
import os
ip = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","Pictures","test pic.jpg")
img = cv2.imread(ip)
imgrgb = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
plt.imshow(imgrgb)
plt.title("Original Image")
plt.show()
gimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
plt.imshow(gimg,cmap = "gray")
plt.title("Grayscale Image")
plt.show()
cimg = imgrgb[450:700,400:700]
crgb = cv2.cvtColor(cimg,cv2.COLOR_BGR2RGB)
plt.imshow(crgb)
plt.title("Cropped Region")
plt.show()
(h,w) = img.shape[:2]
c = (w//2,h//2)
m = cv2.getRotationMatrix2D(c,25,1)
r = cv2.warpAffine(imgrgb,m,(w,h))
rrgb = cv2.cvtColor(r,cv2.COLOR_BGR2RGB)
plt.imshow(rrgb)
plt.title("Rotated Image")
plt.show()
bm = np.ones(img.shape,dtype = "uint8") * 75
br = cv2.add(img,bm)
brrgb = cv2.cvtColor(br,cv2.COLOR_BGR2RGB)
plt.imshow(brrgb)
plt.title("Brighter Image")
plt.show()
cv2.imwrite("Outputs/Grayscale Image.jpg",gimg)
cv2.imwrite("Outputs/Cropped Image.jpg",cimg)
cv2.imwrite("Outputs/Rotated Image.jpg",r)
cv2.imwrite("Outputs/Brighter Image.jpg",br)