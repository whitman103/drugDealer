import cv2
import numpy as np
import matplotlib.pyplot as plt
import random

img=cv2.imread("qgisColumbus.png")


longestArrows=[]


img2=cv2.pyrDown(img)
img2=cv2.pyrDown(img2)
outStreetsMatrix=open("streetMatrix.txt",'w')
outStreetsMatrix.write(str(img2.shape[0])+"\n")
outStreetsMatrix.write(str(img2.shape[1])+"\n")
replaceImg=img2

def erodeImage(img2):
	replaceImg=img2
	for yIndex,data in enumerate(img2):
		for xIndex,xData in enumerate(img2[yIndex]):
			if img2[yIndex][xIndex][0]!=255:
				aroundCheck=False
				if yIndex!=0:
					if img2[yIndex-1][xIndex][0]!=255:
						aroundCheck=True
				if yIndex!=len(img2)-1:
					if(img2[yIndex+1][xIndex][0]!=255):
						aroundCheck=True
				if xIndex!=0:
					if img2[yIndex][xIndex-1][0]!=255:
						aroundCheck=True
				if xIndex!=len(img2[0])-1:
					if img2[yIndex][xIndex+1][0]!=255:
						aroundCheck=True
				if not aroundCheck:
					replaceImg[yIndex][xIndex][0]=255
	return replaceImg
for i in range(20):
	img2=erodeImage(img2)
cv2.imshow("test",img2)
cv2.waitKey(0)
for yIndex,data in enumerate(img2):
	for xIndex, xData in enumerate(img2[yIndex]):
		outStreetsMatrix.write(str(int(img2[yIndex][xIndex][0]!=255))+" ")
	outStreetsMatrix.write("\n")
outStreetsMatrix.close()