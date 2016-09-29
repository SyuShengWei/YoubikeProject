import os
import numpy as np
import matplotlib.pyplot as plt
import Outlier as OL

TravelData 	= list()
HolidayList = list()
RaindayList = list()
TravelList  = list()
TravelList_Without_outlier = list()
OutlierList = list() #outlier is done befor delete the Rain Day and Holiday

#Travel Data
os.chdir('C:/Users/SyuShengWei/Desktop/project/')
inFile = open('TotalTravelOfSystem.txt','r')
titleLine = inFile.readline()
while True:
	theLine = inFile.readline()
	if theLine == '' : break 
	else:
		lineInfo = theLine.split(',')
		infoList = [lineInfo[0],lineInfo[1],int(lineInfo[2]),lineInfo[3].strip('\n')]
		TravelData.append(infoList)
inFile.close
#HolidayList
inFile = open('Holiday.txt','r')
while True:
	theLine = inFile.readline()
	if theLine == '' : break 
	else:
		HolidayList.append(theLine.strip('\n'))
inFile.close
#RaindayList
inFile = open('RainDay.txt','r')
while True:
	theLine = inFile.readline()
	if theLine == '' : break 
	else:
		RaindayList.append(theLine.strip('\n'))
inFile.close

#print(TravelData)
#print(HolidayList)
#print(RaindayList)

for dayInfoList in TravelData:
	if dayInfoList[0] in HolidayList:
		dayInfoList[2] = None 
	if dayInfoList[0] in RaindayList:
		dayInfoList[2] = None

for i in range(0,302) :
	TravelList.append(TravelData[i][2])

#print(TravelList)
TravelList_WithoutRH = list()

for element in TravelList :
	if element != None :
		TravelList_WithoutRH.append(element)

outlierData = list()
outlierData = OL.outlier(TravelList,3,TravelList_WithoutRH)

for i in range(0,302):
	if i in outlierData[0] or i in outlierData[1]:
		OutlierList.append(TravelData[i][0])
		TravelData[i][2] = None


for i in range(0,302) :
	TravelList_Without_outlier.append(TravelData[i][2])

#print(TravelData)
os.chdir('C:/Users/SyuShengWei/Desktop/project/')
outFile = open('OutlierDay.txt','a')
for element in OutlierList:
	outFile.write(element)
	outFile.write('\n')
outFile.close


x = np.arange(0,len(TravelList_Without_outlier))
y = TravelList_Without_outlier

plt.plot(x,y)

std_range = 3
plt.plot([0,350],[outlierData[2] + std_range* outlierData[3],outlierData[2] + std_range* outlierData[3]],lw = 2)
plt.plot([0,350],[outlierData[2] - std_range* outlierData[3],outlierData[2] - std_range* outlierData[3]],lw = 2)

xs = np.arange(0,len(TravelList_Without_outlier))
series1 = np.array(TravelList_Without_outlier).astype(np.double)
s1mask = np.isfinite(series1)

plt.plot(xs[s1mask], series1[s1mask], linestyle='-', marker='o')

plt.xlabel("Day") 
plt.ylabel("Traveling") 
plt.title("Growing of YouBike System_Without holiday and rain") 
	
plt.show()
