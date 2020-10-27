import cv2
import numpy as np
import matplotlib.pyplot as plt
import random
import math

from numpy.lib.function_base import average

"""img=cv2.imread("qgisColumbus.png")


longestArrows=[]


img2=cv2.pyrDown(img)
outStreetsMatrix=open("streetMatrix.txt",'w')
outStreetsMatrix.write(str(img2.shape[0])+"\n")
outStreetsMatrix.write(str(img2.shape[1])+"\n")
replaceImg=img2

radius=15

def findCrossing(radius,img):
	identityImage=img
	for yIndex in range(radius,len(img)-radius-1,1):
		for xIndex in range(radius,len(img[yIndex])-radius-1,1):
			if img[yIndex][xIndex][0]!=255:
				count=0
				cornerCheck=int(img[yIndex+radius][xIndex+radius][0]==255)+int(img[yIndex+radius][xIndex-radius][0]==255)+int(img[yIndex-radius][xIndex+radius][0]==255)+int(img[yIndex-radius][xIndex-radius][0]==255)
				if cornerCheck>3:
					sweepCheck=[False,False,False,False]
					for i in range(2*radius):
						if img[yIndex+i-radius][xIndex-radius][0]!=255 and not sweepCheck[1]:
							sweepCheck[0]=True
						if img[yIndex+i-radius][xIndex+radius][0]!=255 and not sweepCheck[0]:
							sweepCheck[1]=True
						if img[yIndex-radius][xIndex-radius+i][0]!=255 and not sweepCheck[3]:
							sweepCheck[2]=True
						if img[yIndex+radius][xIndex-radius+i][0]!=255 and not sweepCheck[2]:
							sweepCheck[3]=True
					for entry in sweepCheck:
						count+=int(entry)
				if count>1:
					identityImage[yIndex][xIndex]=[0,0,0]
	return identityImage
				
				
foundImg=findCrossing(radius,img2)
cv2.imwrite("crossingImage.png",foundImg)"""

foundImg=cv2.imread("crossingImage.png")
cv2.imshow("FoungImg",foundImg)

def returnAdjacency(x,y):
	return [[x,y-1],[x,y+1],[x+1,y],[x-1,y]]

def consolidateCrossings(img):
	crossingDictionary=[[]]
	numberOfCrossing=0
	for yIndex,yData in enumerate(img):
		for xIndex,xData in enumerate(img[yIndex]):
			if img[yIndex][xIndex][0]==0:
				newEntry=True
				adjacencyCheck=returnAdjacency(yIndex,xIndex)
				for crossIndex,crossing in enumerate(crossingDictionary):
					for neighbor in adjacencyCheck:
						if neighbor in crossing and [yIndex,xIndex] not in crossing:
							crossingDictionary[crossIndex].append([yIndex,xIndex])
							newEntry=False
				if newEntry:
					crossingDictionary[numberOfCrossing].append([yIndex,xIndex])
					numberOfCrossing+=1
					crossingDictionary.append([])
	return crossingDictionary

"""crossingIdentities=consolidateCrossings(foundImg)


def findCentroids(inArray):
	centroids=[[]]
	for crossing in inArray:
		xMean,yMean=0,0
		for element in crossing:
			xMean+=element[1]/len(crossing)
			yMean+=element[0]/len(crossing)
		centroids.append([math.floor(yMean),math.floor(xMean)])
	return centroids
	
centroids=findCentroids(crossingIdentities)



outFile=open("baseCentroids.txt",'w')
centroids.pop(0)
for element in centroids:
	outFile.write(str(element[0])+" "+str(element[1])+"\n")
outFile.close()"""

def loadCentroids(inString):

	centroids=[]
	inString=open(inString,'r')
	for line in inString:
		line=line.split(" ")
		line[1]=line[1].split("\n")[0]
		centroids.append([int(line[0]),int(line[1])])
	return centroids


centroids=loadCentroids("baseCentroids.txt")

testCentroids=foundImg

for yIndex,yData in enumerate(foundImg):
	for xIndex,xData in enumerate(foundImg[yIndex]):
		if [yIndex,xIndex] in centroids:
			testCentroids[yIndex][xIndex]=[0,255,0]
		else:
			testCentroids[yIndex][xIndex]=[0,0,0]

cv2.imshow("greenTest",testCentroids)



def distance(x1,y1,x2,y2):
	return math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))

def averageCentroids(minDistance,inCentroids):
	mergeList=[[] for i in range(len(inCentroids))]
	for firstIndex,firstData in enumerate(inCentroids):
		selfInclude=True
		for secondIndex,secondData in enumerate(inCentroids):
			if distance(inCentroids[firstIndex][0],inCentroids[firstIndex][1],inCentroids[secondIndex][0],inCentroids[secondIndex][1])<minDistance:
				mergeList[firstIndex].append(secondIndex)
		
			
	finalList=[]
	checkBack=[i for i in range(len(inCentroids))]
	for mergeIndex,group in enumerate(mergeList):
		if mergeIndex==0:
			finalList.append(group)
		for element in group:
			appendGroup=True
			for finalIndex,finalGroup in enumerate(finalList):
				if element in finalGroup:
					finalList[finalIndex]+=list(set(group)-set(finalGroup))
					appendGroup=False
			if appendGroup:
				finalList.append(group)
	print(finalList)
	outList=[]
	for mergeGroup in finalList:
		xMean,yMean=0,0
		for index in mergeGroup:
			xMean+=inCentroids[index][1]/len(mergeGroup)
			yMean+=inCentroids[index][0]/len(mergeGroup)
		outList.append([int(yMean),int(xMean)])
	outList.pop(0)
	return outList


centroids=averageCentroids(15,centroids)






mergedCentroids=foundImg
for yIndex,yData in enumerate(mergedCentroids):
	for xIndex,xData in enumerate(mergedCentroids[yIndex]):
		if [yIndex,xIndex] in centroids:
			for xSweep in range(-1,2,1):
				for ySweep in range(-1,2,1):
					mergedCentroids[yIndex+ySweep][xIndex+xSweep]=[255,0,0]
		else:
			if mergedCentroids[yIndex][xIndex][0]!=255:
				mergedCentroids[yIndex][xIndex]=[0,0,0]



cv2.imshow("Compare",mergedCentroids)
cv2.waitKey(0)

"""for yIndex,data in enumerate(img2):
	for xIndex, xData in enumerate(img2[yIndex]):
		outStreetsMatrix.write(str(int(img2[yIndex][xIndex][0]!=255))+" ")
	outStreetsMatrix.write("\n")
outStreetsMatrix.close()"""