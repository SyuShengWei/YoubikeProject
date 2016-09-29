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
			#peroid_time = int(Line_Info[1])
			#peroid_index = int(peroid_time/NUM_peroid_time)
			traveling_time = int(Line_Info[10])
			TravelingMatrix[o_index][d_index].append(traveling_time)

AverageMatrix = list()			
for O in range(0,NUM_station):
	O_List = list()
	for D in range(0,NUM_station):
		D_List = 0
		O_List.append(D_List)
	AverageMatrix.append(O_List)
			
for O in range(0,NUM_station):			
	for D in range(0,NUM_station):
		if len(TravelingMatrix[O][D]) == 0 :
			continue
		else :
			Test_List = TravelingMatrix[O][D]
			OutLierResult = outlier(Test_List,3)
			total_value = 0
			total_num   = 0
			for index in range(0,len(Test_List)):
				if index not in OutLierResult[0] and index not in OutLierResult[1]:
					total_value += Test_List[index]
					total_num +=1
			average_value = round(total_value / total_num,3)
			AverageMatrix[O][D] = average_value
			
outFile = open('C:/Users/SyuShengWei/Desktop/project/Traveling_Time_Average.txt','a')
for O in range(0,NUM_station):
	for D in range(0,NUM_station):
		if AverageMatrix[O][D] == 0 : outFile.write('non')
		else: outFile.write(str(AverageMatrix[O][D]))
		
		if D != NUM_station -1 : outFile.write(' ')
		else : outFile.write('\n')