import os 
import numpy as np
import matplotlib.pyplot as plt

TravelList = list()
AveraveCTR   = 0
AverageValue = 0

inFile = open('C:/Users/SyuShengWei/Desktop/project/TotalTravelOfSystem.txt','r')
titleLine = inFile.readline()
while True :
	theLine = inFile.readline()
	if theLine == '': break 
	else :
		lineInfo = theLine.split(',')
		TravelList.append(int(lineInfo[1].strip('\n')))
		AveraveCTR += 1
		AverageValue += int(lineInfo[1].strip('\n'))

AverageValue = AverageValue / AveraveCTR


theList = [0,1,1,3,8,10,12]
x = np.arange(0,len(theList))
y = theList

fig = plt.figure()
ax = fig.add_subplot(111)
t = ax.scatter(np.random.rand(20), np.random.rand(20))
#fig.show()
fig.savefig('C:/Users/SyuShengWei/Desktop/project/001.png')

fig = plt.figure()
ax = fig.add_subplot(111)
t = ax.plot(x,y,'ro')
t = ax.plot(x,y)
#fig.show()
fig.savefig('C:/Users/SyuShengWei/Desktop/project/002.png')