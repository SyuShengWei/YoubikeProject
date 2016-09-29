import os 
from Outlier import *


NUM_station 	= 164
NUM_peroid 		= 24
NUM_peroid_time = 24*60*60 / NUM_peroid

TravelingMatrix = list()

for O in range(0,NUM_station):
	O_List = list()
	for D in range(0,NUM_station):
		D_List = list()
		for peroid in range(0,NUM_peroid):
			Peroid_List = list()
			D_List.append(Peroid_List)
		O_List.append(D_List)
	TravelingMatrix.append(O_List)

Normal_Day_List = list()
inFile = open('C:/Users/SyuShengWei/Desktop/project/NormalDay.txt','r')
Data_List = inFile.readlines()
for DataLine in Data_List:
	theLine = DataLine.strip('\n')
	Normal_Day_List.append(theLine)
	
for filename in os.listdir('C:/Users/SyuShengWei/Desktop/project/RegularForm'):
	
	the_day = filename.strip('.csv')
	if the_day not in Normal_Day_List : continue
	else:
		os.chdir('C:/Users/SyuShengWei/Desktop/project/RegularForm')
		inFile = open(filename,'r')
		titleLine = inFile.readline()
		Data_List = inFile.readlines()
		for DataLine in Data_List:
			theLine = DataLine.strip('\n')
			Line_Info = theLine.split(',')
			o_index 	= int(Line_Info[4])
			d_index 	= int(Line_Info[5])
			peroid_time = int(Line_Info[1])
			peroid_index = int(peroid_time/NUM_peroid_time)
			traveling_time = int(Line_Info[10])
			TravelingMatrix[o_index][d_index][peroid_index].append(traveling_time)

zero_data = 0
well_data =	NUM_station * NUM_station *	NUM_peroid	
			
for O in range(0,NUM_station):			
	for D in range(0,NUM_station):
		for peroid in range(0,NUM_peroid):
			if len(TravelingMatrix[O][D][peroid]) == 0 :
				print(str(O)+','+str(D)+','+str(peroid))
				zero_data += 1

well_data -= zero_data
print('zero_data',end='')
print(zero_data)
print('well_data',end='')
print(well_data)				