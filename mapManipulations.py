import cv2
import numpy as np
import math


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

def findCentroids(inArray):
	centroids=[[]]
	for crossing in inArray:
		xMean,yMean=0,0
		for element in crossing:
			xMean+=element[1]/len(crossing)
			yMean+=element[0]/len(crossing)
		centroids.append([math.floor(yMean),math.floor(xMean)])
	return centroids

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

def loadCentroids(inString):



	centroids=[]
	inString=open(inString,'r')
	inString.readline()
	for line in inString:
		line=line.split(" ")
		line[1]=line[1].split("\n")[0]
		centroids.append([int(line[0]),int(line[1])])
	return centroids

def distance(x1,y1,x2,y2):
	return math.sqrt(pow(x1-x2,2)+pow(y1-y2,2))

def s1Distance(x1,y1,x2,y2):
	return math.fabs(x1-x2)+math.fabs(y1-y2)

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

def drawLines(maxDistance,inCentroids,inMetric):
	maxConnections=4
	distanceLabels=[[] for i in range(len(inCentroids))]
	for firstIndex,firstCen in enumerate(inCentroids):
		y1,x1=inCentroids[firstIndex][0],inCentroids[firstIndex][1]
		for secondIndex,secondCen in enumerate(inCentroids):
			y2,x2=inCentroids[secondIndex][0],inCentroids[secondIndex][1]
			distanceLabels[firstIndex].append([y1-y2,x1-x2])
			if firstIndex==secondIndex:
				distanceLabels[firstIndex][secondIndex]=[1e23,1e23]
	indexConnections=[[-11,-11,-11,-11] for i in range(len(inCentroids))]
	for baseIndex,baseNode in enumerate(distanceLabels):
		negX,negY,posX,posY=-1e10,-1e10,1e10,1e10
		for compareIndex,compare in enumerate(distanceLabels[baseIndex]):
			compareDistance=math.sqrt(pow(compare[0],2)+pow(compare[1],2))
			if compareDistance<maxDistance:
				if compare[0]<posX and compare[0]>0:
					indexConnections[baseIndex][0]=compareIndex
					posX=compare[0]
				if compare[0]>negX and compare[0]<0:
					indexConnections[baseIndex][1]=compareIndex
					negX=compare[0]
				if compare[1]<posY and compare[1]>0:
					indexConnections[baseIndex][2]=compareIndex
					posY=compare[1]
				if compare[1]>negY and compare[1]<0:
					indexConnections[baseIndex][3]=compareIndex
					negY=compare[1]
	for index,out in enumerate(indexConnections):
		while -11 in out:
			indexConnections[index].remove(-11)
	return indexConnections


