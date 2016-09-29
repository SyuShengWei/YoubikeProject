import os 

TravelRecord = list()
for day in range(0,302):
	Day_List = list()
	for peroid in range(0,96):
		Peroid_List = list()
		for station in range(0,164):
			return_record = 0
			Peroid_List.append(return_record)
		Day_List.append(Peroid_List)
	TravelRecord.append(Day_List)

Day_Name_List = list()	

Station_Name_List = list()
for filename in os.listdir('C:/Users/SyuShengWei/Desktop/project/RegularSplitByStation'):
	Station_Name_List.append(filename)

day_index = 0

for filename in os.listdir('C:/Users/SyuShengWei/Desktop/project/RegularForm'):
	
	os.chdir('C:/Users/SyuShengWei/Desktop/project/RegularForm')
	inFile = open(filename,'r')
	titleLine = inFile.readline()
	Data_List = inFile.readlines()
	for Data_Line in Data_List :
		theLine = Data_Line.strip('\n')
		Line_Info = theLine.split(',')
		return_peroid = int(int(Line_Info[3])/900)
		return_station = int(Line_Info[5])
		TravelRecord[day_index][return_peroid][return_station] += 1
	inFile.close()	
	
	
	day_name = filename.strip('.csv')
	Day_Name_List.append(day_name)
	day_index += 1

#print(Day_Name_List)	
	
os.chdir('C:/Users/SyuShengWei/Desktop/project')
if not os.path.exists('Data_Return_15min'):
	os.makedirs('Data_Return_15min')
os.chdir('C:/Users/SyuShengWei/Desktop/project/Data_Return_15min')

for station in range(0,164):
	outFile = open(Station_Name_List[station] + '.csv','a')
	outFile.write('Date,Peroid,Return\n')
	for day in range(0,302):
		for peroid in range(0,96):
			outLine = Day_Name_List[day] + ',' + str(peroid) + ',' + str(TravelRecord[day][peroid][station]) + '\n' 
			outFile.write(outLine)
	