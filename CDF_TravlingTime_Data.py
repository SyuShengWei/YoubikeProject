import os 
from Outlier import *

TravelingTimeDataMatrix = list()
for i in range (0,164):
	distinationList = list()
	for j in range(0,164):
		eachKindDataList = list()
		for k in range(0,4):
			dataList = list()
			eachKindDataList.append(dataList)
		distinationList.append(eachKindDataList)
	TravelingTimeDataMatrix.append(distinationList)

Temp_TravelingTimeDataMatrix = list()
for i in range (0,164):
	distinationList = list()
	for j in range(0,164):
		eachKindDataList = list()
		for k in range(0,4):
			dataList = list()
			eachKindDataList.append(dataList)
		distinationList.append(eachKindDataList)
	Temp_TravelingTimeDataMatrix.append(distinationList)
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

flodNum = 0
#start to scan data
for folder in os.listdir('C:/Users/SyuShengWei/Desktop/project/RegularSplitByStation'):
	print('The Station :' + str(flodNum))
	flodNum += 1
	for filename in os.listdir('C:/Users/SyuShengWei/Desktop/project/RegularSplitByStation/'+folder):
		theDay = filename.strip('.csv')
		if theDay in OutlierList :
			continue
		elif theDay not in RaindayList and theDay not in HolidayList :
			dataKind = 0 #沒下雨、非假日 (0,0)
		elif theDay  in RaindayList and theDay not in HolidayList :
			dataKind = 1 # 下雨、非假日 (1,0)
		elif theDay not in RaindayList and theDay  in HolidayList :
			dataKind = 2 #沒下雨、 假日 (0,1)
		elif theDay  in RaindayList and theDay  in HolidayList :
			dataKind = 3 # 下雨、 假日 (1,1)
		os.chdir('C:/Users/SyuShengWei/Desktop/project/RegularSplitByStation/'+folder)
		inFile = open(filename)
		titleLine = inFile.readline()
		while True:
			theLine = inFile.readline()
			if theLine == '' :
				break
			else :
				lineInfo = theLine.split(',')
				OIndex = int(lineInfo[4])
				DIndex = int(lineInfo[5])
				travelingTime = int(lineInfo[10].strip('\n'))
				#print(str(OIndex)+','+str(DIndex)+','+str(dataKind))
				Temp_TravelingTimeDataMatrix[OIndex][DIndex][dataKind].append(travelingTime)
	
for i in range (0,164):
	for j in range (0,164):
		for k in range (0,4):
			tempList = Temp_TravelingTimeDataMatrix[i][j][k]
			if tempList == [] :
				continue
			else:
				outlierData = outlier(tempList)
			for x in range (0,len(tempList)):
				if x in outlierData[0] or x in outlierData[1]:
					continue
				else :
					TravelingTimeDataMatrix[i][j][k].append(tempList[x])

os.chdir('C:/Users/SyuShengWei/Desktop/project')
outFile = open ('CDF_Data.txt','a')
for i in range (0,164):
	for j in range (0,164):
		for k in range (0,4):
			if k == 3 :
				if len(TravelingTimeDataMatrix[i][j][k]) == 0:
					outFile.write('-1')
				else :
					for x in range(0,len(TravelingTimeDataMatrix[i][j][k])-1):
						outFile.write(str(TravelingTimeDataMatrix[i][j][k][x]))
						outFile.write(',')
					outFile.write(str(TravelingTimeDataMatrix[i][j][k][len(TravelingTimeDataMatrix[i][j][k])-1]))
				outFile.write('\n')
			else:
				if len(TravelingTimeDataMatrix[i][j][k]) == 0:
					outFile.write('-1')
				else :
					for x in range(0,len(TravelingTimeDataMatrix[i][j][k])-1):
						outFile.write(str(TravelingTimeDataMatrix[i][j][k][x]))
						outFile.write(',')
					outFile.write(str(TravelingTimeDataMatrix[i][j][k][len(TravelingTimeDataMatrix[i][j][k])-1]))
				outFile.write('+')
			
outFile.close()


