import cv2
import numpy as np
import matplotlib.pyplot as plt
import random
import math
import mapManipulations as mapFunctions

from numpy.lib.function_base import average

"""img=cv2.imread("qgisColumbus.png")
img2=cv2.pyrDown(img)
outStreetsMatrix=open("streetMatrix.txt",'w')
outStreetsMatrix.write(str(img2.shape[0])+"\n")
outStreetsMatrix.write(str(img2.shape[1])+"\n")
replaceImg=img2
radius=15		
foundImg=findCrossing(radius,img2)
cv2.imwrite("crossingImage.png",foundImg)
crossingIdentities=consolidateCrossings(foundImg)
centroids=findCentroids(crossingIdentities)"""

foundImg=cv2.imread("crossingImage.png")

centroids=mapFunctions.loadCentroids("finalNodes.txt")
mergedCentroids=foundImg
for yIndex,yData in enumerate(mergedCentroids):
	for xIndex,xData in enumerate(mergedCentroids[yIndex]):
		if [yIndex,xIndex] in centroids:
			for xSweep in range(-1,2,1):
				for ySweep in range(-1,2,1):
					mergedCentroids[yIndex+ySweep][xIndex+xSweep]=[255,0,0]
		

cv2.imshow("Identitfied",mergedCentroids)
cv2.waitKey(0)















