import os 
from Outlier import *

TravelingTimeDataMatrix = list()
for O in range (0,164):
	distinationList = list()
	for D in range(0,164):
		eachKindDataList = list()
		for Type in range(0,4):
			dataList = list()
			for Peroid in range(0,96):
				peroidList = list()
				dataList.append(peroidList)
			eachKindDataList.append(dataList)
		distinationList.append(eachKindDataList)
	TravelingTimeDataMatrix.append(distinationList)
	
Temp_TravelingTimeDataMatrix = list()
for O in range (0,164):
	distinationList = list()
	for D in range(0,164):
		eachKindDataList = list()
		for Type in range(0,4):
			dataList = list()
			for Peroid in range(0,96):
				peroidList = list()
				dataList.append(peroidList)
			eachKindDataList.append(dataList)
		distinationList.append(eachKindDataList)
	Temp_TravelingTimeDataMatrix.append(distinationList)
	
ODRateDataMatrix = list()
for O in range (0,164):
	distinationList = list()
	for D in range(0,164):
		eachKindDataList = list()
		for Type in range(0,4):
			dataList = list()
			for Peroid in range(0,96):
				peroidList = 0
				dataList.append(peroidList)
			eachKindDataList.append(dataList)
		distinationList.append(eachKindDataList)
	ODRateDataMatrix.append(distinationList)

ODTotalMatrix = list()
#only O to store the total rent of one station
for O in range (0,164):
	eachKindDataList = list()
	for Type in range(0,4):
		dataList = list()
		for Peroid in range(0,96):
			peroidList = 0
			dataList.append(peroidList)
		eachKindDataList.append(dataList)
	ODTotalMatrix.append(eachKindDataList)	

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

for filename in os.listdir('C:/Users/SyuShengWei/Desktop/project/RegularForm'):
	
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
		
	os.chdir('C:/Users/SyuShengWei/Desktop/project/RegularForm')
	inFile = open(filename,'r')
	titleLine = inFile.readline()
	dataList = inFile.readlines()
	for theLine in dataList:
		theLine = theLine.strip('\n')
		lineInfo = theLine.split(',')
		rentTimeImdex = int(int(lineInfo[1])/900)
		OIndex = int(lineInfo[4])
		DIndex = int(lineInfo[5])
		travelingTime = int(lineInfo[10])
		Temp_TravelingTimeDataMatrix[OIndex][DIndex][dataKind][rentTimeImdex].append(travelingTime)
		ODRateDataMatrix[OIndex][DIndex][dataKind][rentTimeImdex] += 1
		ODTotalMatrix[OIndex][dataKind][rentTimeImdex] += 1
	
#print(Temp_TravelingTimeDataMatrix)


for i in range (0,164):
	for j in range (0,164):
		for k in range (0,4):
			for l in range(0,96):
				tempList = Temp_TravelingTimeDataMatrix[i][j][k][l]
				if tempList == [] :
					continue
				else:
					outlierData = outlier(tempList)
				for x in range (0,len(tempList)):
					if x in outlierData[0] or x in outlierData[1]:
						continue
					else :
						TravelingTimeDataMatrix[i][j][k][l].append(tempList[x])
	
'''
for O in range(0,164):
	os.chdir('C:/Users/SyuShengWei/Desktop/project/Analysis_Peroid_ODandTraveling')
	if not os.path.exists('station'+str(O).rjust(3,"0")):
		os.makedirs('station'+str(O).rjust(3,"0"))
	os.chdir('C:/Users/SyuShengWei/Desktop/project/Analysis_Peroid_ODandTraveling/'+'station'+str(O).rjust(3,"0"))
	
	for D in range(0,164):
		outFile = open(str(D).rjust(3,"0")+'.txt','a')
		for peroid in range(0,96):
			outLine = list()
			outAverage = list()
			for Type in range(0,4):
				if ODTotalMatrix[O][Type][peroid] != 0:
					theODRate = round(ODRateDataMatrix[O][D][Type][peroid] / ODTotalMatrix[O][Type][peroid],4)
				else :
					theODRate = round(0,4)
				outLine.append(theODRate)
				
			outFile.write(str(outLine[0])+' , '+str(outLine[1])+' , '+str(outLine[2])+' , '+str(outLine[3])+'\n')
		outFile.close()

	try:
		for D in range (0,164):
			os.chdir('C:/Users/SyuShengWei/Desktop/project/Analysis_Peroid_ODandTraveling/'+'station'+str(O).rjust(3,"0"))
			if not os.path.exists(str(D).rjust(3,"0")):
				os.makedirs(str(D).rjust(3,"0"))
			os.chdir('C:/Users/SyuShengWei/Desktop/project/Analysis_Peroid_ODandTraveling/'+'station'+str(O).rjust(3,"0")+'/'+str(D).rjust(3,"0")+'/')
			for Type in range(0,4):
				fig = plt.figure()
				ax = fig.add_subplot(111)
				for P in range(0,96):
					plotList = list()
					plotList = TravelingTimeDataMatrix[O][D][Type][P]
					if plotList == [] :
						continue
					else :
						plotList.sort()
						x = list()
						prob = 1 / len(plotList) 
						for len in range(0,len(plotList)):
							x.append((len+1)*prob)
						t = ax.plot(x,plotList)
				fig.savefig(str(Type)+'.png')
				plt.close(fig)
	except:
		print('error')
	'''
os.chdir('C:/Users/SyuShengWei/Desktop/project/Analysis_Peroid_ODandTraveling')

outFile = open('TravelingTimePeroid.txt','a')
for i in range (0,164):
	for j in range (0,164):
		for l in range(0,96):
			outFile.write(str(l).rjust(2,'0')+' : ')
			outLine = list()
			for k in range(0,4):
				if TravelingTimeDataMatrix[i][j][k][l] != [] :
					Array_data = np.asarray(TravelingTimeDataMatrix[i][j][k][l])
					Data_average = np.mean(Array_data)
				else:
					Data_average = 0
				outLine.append(Data_average)
			outFile.write(str(outLine[0])+' , ' +str(outLine[1])+' , ' +str(outLine[2])+' , ' +str(outLine[3])+' , ' +'\n') 
		
		
