'''
This file is used to calculate the CDF　probability
Prepare File : CDF_Data.txt
Input :	1.O station
		2.D station
		3.X value
Output: the probability that the Traveling time is smaller then x 
'''
import os 
from CDF import *


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
#input data
print('Reading InFile')
os.chdir('C:/Users/SyuShengWei/Desktop/project') #you can change you path here
inFile = open('CDF_Data.txt','r')
theData = inFile.readlines()
for i in range(0,len(theData)):
	OIndex = int(i / 164)
	DIndex = i % 164
	theData[i] = theData[i].strip('\n')
	anODData = theData[i].split('+')
	for k in range(0,4):
		aKindData = anODData[k].split(',')
		for element in aKindData:
			if element != '-1':
				TravelingTimeDataMatrix[OIndex][DIndex][k].append(int(element))
			else :
				continue
#receive input 
end_control = '1'
while end_control != '0' :
	if_rain    = int(input('Please Input If You Want Rainday data(0->No,1->Yes):'))
	if_holiday = int(input('Please Input If You Want Holiday data(0->No,1->Yes):'))
	if if_rain == 0 and if_holiday == 0:
		dataKind = 0
	elif if_rain == 1 and if_holiday == 0:
		dataKind = 1
	elif if_rain == 0 and if_holiday == 1:
		dataKind = 2
	elif if_rain == 1 and if_holiday == 1:
		dataKind = 3
	else:
		print('wrong input , please try again')
		continue
	print('Please input the O ,D and X ')
	print('the value is the porbility the Traveling Time will with in X(s) ')
	O_station = int(input('Please Input The O_Station(0-163):'))
	D_station = int(input('Please Input The D_Station(0-163):'))
	if O_station not in range(0,164) or D_station not in range(0,164):
		print('wrong input , please try again')
		continue
	
	if len(TravelingTimeDataMatrix[O_station][D_station][dataKind]) == 0 :
		print('Have no data ,try another')
		continue
	X_value   = int(input('Please Input The X_value :'))
	
	#print(TravelingTimeDataMatrix[O_station][D_station][dataKind])
	theCDF = CDF(TravelingTimeDataMatrix[O_station][D_station][dataKind])
	#print(theCDF.dataList)
	the_probability = theCDF.prob_within_X(X_value,10)
	#print(the_probability)
	print('O_Station : ' + str(O_station) +',' + 'D_Station : ' + str(D_station) + ',' +'probability that traveling time within ' + str(X_value) +' : '+str(the_probability))
	end_control = input('Continue?(input 0 to leave)')