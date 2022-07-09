import cv2
import numpy

img_path = "/home/raito/Documents/College Shitz/OCR GR 1/Tools/Japanese-OCR/Selecting_ROI/Img/img.jpg"

img_raw=cv2.imread(img_path)
roi=cv2.selectROI(img_raw)
print(str(roi[1])+':'+str(roi[1]+roi[3])+','+ str(roi[0])+":"+str(roi[0]+roi[2]))