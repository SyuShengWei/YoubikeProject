import os 

os.chdir('C:/Users/SyuShengWei/Desktop/project/')
#normal day List
Normal_Day_List = list()
inFile = open('NormalDay.txt','r')
Data_List = inFile.readlines()
for theLine in Data_List:
	Normal_Day_List.append(theLine.strip('\n'))
inFile.close()

NUM_normalday = len(Normal_Day_List)
NUM_peroid    = 48
NUM_station   = 164
NUM_lenofperoid = 3600

Perday_ODRRecord = list()
for day in range(0,NUM_normalday):
	ODRRecord = list()
	for O in range(0,NUM_station):
		O_List = list()
		for D in range(0,NUM_station):
			D_List = list()
			for peroid in range(0,NUM_peroid):
				peroid_record = 0
				D_List.append(peroid_record)
			O_List.append(D_List)
		ODRRecord.append(O_List)
	Perday_ODRRecord.append(ODRRecord)

Perday_TotalRecord = list()
for day in range(0,NUM_normalday):
	Total_ODRecord = list()	
	for O in range(0,NUM_station):
		O_List = list()
		for peroid in range(0,NUM_peroid):
			peroid_record = 0
			O_List.append(peroid_record)
		Total_ODRecord.append(O_List)	
	Perday_TotalRecord.append(Total_ODRecord)
	
for filename in os.listdir('C:/Users/SyuShengWei/Desktop/project/RegularForm'):
	os.chdir('C:/Users/SyuShengWei/Desktop/project/RegularForm')
	the_day = filename.strip('.csv')
	if the_day not in Normal_Day_List : continue
	else :
		day_index = Normal_Day_List.index(the_day)
		inFile = open(filename,'r')
		titelLine = inFile.readline()
		Data_List = inFile.readlines()
		for dataLine in Data_List:
			theLine = dataLine.strip('\n')
			Line_Info = theLine.split(',')
			o_index = int(Line_Info[4])
			d_index = int(Line_Info[5])
			peroid_index =  int(Line_Info[1])//NUM_lenofperoid
			
			Perday_ODRRecord[day_index][o_index][d_index][peroid_index] 	+= 1
			Perday_TotalRecord[day_index][o_index][peroid_index] 			+= 1
		
		inFile.close()

	
Top_10_Station_List = list()   #[day][O][peroid][i]
Top_10_Value_List = list()
for day in range(0,NUM_normalday):
	Day_List = list()
	for O in range(0,NUM_station):
		O_List = list()
		for peroid in range(0,NUM_peroid):
			Peroid_List = list()
			for i in range(0,10):
				Peroid_List.append(-1)
			O_List.append(Peroid_List)
		Day_List.append(O_List)
	Top_10_Station_List.append(Day_List)
	Top_10_Value_List.append(Day_List)

for day in range(0,NUM_normalday):
	for O in range(0,NUM_station):
		for D in range(0,NUM_station):
			for peroid in range(0,NUM_peroid):
				for index in range(0,10):
					if Perday_ODRRecord[day][O][D][peroid] >= Top_10_Value_List[day][O][peroid][index] :
						Top_10_Value_List[day][O][peroid].insert(index,Perday_ODRRecord[day][O][D][peroid])
						Top_10_Station_List[day][O][peroid].insert(index,D)
						lose_value = Top_10_Value_List[day][O][peroid].pop()
						lose_Station = Top_10_Station_List[day][O][peroid].pop()
						break
					else:
						continue
						
os.chdir('C:/Users/SyuShengWei/Desktop/project/Analysis/Top1to3')	
for O in range(NUM_station):
	outFile = open(str(O).rjust(3,'0')+'.csv','a')
	for peroid in range(0,NUM_peroid):
		for day in range(0,NUM_normalday):
			outFile.write(str(Top_10_Station_List[day][O][peroid][0]).rjust(3,'0') + '_' + str(Top_10_Station_List[day][O][peroid][1]).rjust(3,'0') + '_' + str(Top_10_Station_List[day][O][peroid][2]).rjust(3,'0'))
			if day != NUM_normalday -1 :
				outFile.write(',')
			else :
				outFile.write('\n')