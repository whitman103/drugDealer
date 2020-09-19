import cv2
import numpy as np
import matplotlib.pyplot as plt
import random

img=cv2.imread("qgisColumbus.png")


longestArrows=[]


img2=cv2.pyrDown(img)
img2=cv2.pyrDown(img2)
print(img2.shape)
outStreetsMatrix=open("streetMatrix.txt",'w')
outStreetsMatrix.write(str(img2.shape[0])+"\n")
outStreetsMatrix.write(str(img2.shape[1])+"\n")
for yIndex,data in enumerate(img2):
	for xIndex, xData in enumerate(img2[yIndex]):
		outStreetsMatrix.write(str(int(img2[yIndex][xIndex][0]!=255))+" ")
	outStreetsMatrix.write("\n")
outStreetsMatrix.close()