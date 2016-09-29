import os 
import numpy as np
import matplotlib.pyplot as plt
#input Holiday RainDay Outliser	
os.chdir('C:/Users/SyuShengWei/Desktop/project')

#Holiday list
HolidayList = list()
inFile = open('Holiday.txt','r')
while True:
	theLine = inFile.readline()
	if theLine == '' : break
	else : HolidayList.append(theLine.strip('\n'))
inFile.close()

#RainDay list
RaindayList = list()
inFile = open('RainDay.txt','r')
while True:
	theLine = inFile.readline()
	if theLine == '' : break
	else : RaindayList.append(theLine.strip('\n'))
inFile.close()

#Outlier List 
OutlierList = list()
inFile = open('OutlierDay.txt','r')
while True:
	theLine = inFile.readline()
	if theLine == '' : break
	else : OutlierList.append(theLine.strip('\n'))
inFile.close()

#Weekday List
WeekdayList = list()
for i in range(0,365):
	if (i+3) % 7 == 0 :
		WeekdayList.append(7)
	else:
		WeekdayList.append((i+3) % 7)

ArrivalRateDataMatrix = list()
for station in range (0,164):
	stationList = list()
	for weekday in range(0,7):
		weeklydayList = list()
		for datatype in range(0,4):
			dataList = list()
			weeklydayList.append(dataList)
		stationList.append(weeklydayList)
	ArrivalRateDataMatrix.append(stationList)

		
	
'''
TravelingTimeDataMatrix = list()
for i in range (0,164):
	distinationList = list()
	for j in range(0,164):
		eachKindDataList = list()
		for k in range(0,4):
			dataList = list()
			for l in range(0,96):
				peroidList = list()
				dataList.append(peroidList) 
			eachKindDataList.append(dataList)
		distinationList.append(eachKindDataList)
	TravelingTimeDataMatrix.append(distinationList)		
'''
		
		
dayIndex = 0
for filename in os.listdir('C:/Users/SyuShengWei/Desktop/project/RegularForm'):
	
	DayDataList = list()
	for station in range(0,164):
		DayList = list()
		for peroid in range(0,288):
			peroidData = 0
			DayList.append(peroidData)
		DayDataList.append(DayList)
	
	theDay = filename.strip('.csv')
	theWeekday = WeekdayList[dayIndex] - 1
	
	if theDay in OutlierList :
			continue
	elif theDay not in RaindayList and theDay not in HolidayList :
		dataType = 0 #沒下雨、非假日 (0,0)
	elif theDay  in RaindayList and theDay not in HolidayList :
		dataType = 1 # 下雨、非假日 (1,0)
	elif theDay not in RaindayList and theDay  in HolidayList :
		dataType = 2 #沒下雨、 假日 (0,1)
	elif theDay  in RaindayList and theDay  in HolidayList :
		dataType = 3 # 下雨、 假日 (1,1)
		
	os.chdir('C:/Users/SyuShengWei/Desktop/project/RegularForm')	
	inFile = open (filename,'r')
	titleLine = inFile.readline()
	InFileData = inFile.readlines()
	for theLine in InFileData :
		theLine = theLine.strip('\n')
		lineInfo = theLine.split(',')
		rentStationIndex = int(lineInfo[4])
		rentTimeIndex = int(int(lineInfo[1])/300)
		DayDataList[rentStationIndex][rentTimeIndex] += 1
	
	for i in range(0,164):
		ArrivalRateDataMatrix[i][theWeekday][dataType].append(DayDataList[i])
	
	dayIndex += 1


picList = list()
for i in range(0,288):
	picList.append(i)
	
	


	
theList = list()
for j in range(0,len(ArrivalRateDataMatrix[1][2][3])):
	theList = ArrivalRateDataMatrix[1][2][3][j]
	x = np.arange(0,len(theList))
	y = theList
	plt.plot(x,y)
	plt.plot(x,y,'ro')
	
plt.show()	