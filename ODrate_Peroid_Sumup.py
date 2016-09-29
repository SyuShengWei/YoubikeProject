import os 

ODRecord = list()
for O in range(0,164):
	O_List = list()
	for D in range(0,164):
		D_List = list()
		for peroid in range(0,96):
			Record = 0
			D_List.append(Record)
		O_List.append(D_List)
	ODRecord.append(O_List)

Total_ODRecord = list()
for O in range(0,164):
	O_List = list()
	for peroid in range(0,96):
		Total_Record = 0
		O_List.append(Total_Record)
	Total_ODRecord.append(O_List)

for filename in os.listdir('C:/Users/SyuShengWei/Desktop/project/RegularForm'):
	os.chdir('C:/Users/SyuShengWei/Desktop/project/RegularForm')
	inFile = open(filename,'r')
	titleLine = inFile.readline()
	Data_List = inFile.readlines()
	for line_data in Data_List:
		theLine = line_data.strip('\n')
		Line_Info = theLine.split(',')
		rent_peroid = int(int(Line_Info[1])/900)
		o_index = int(Line_Info[4])
		d_index = int(Line_Info[5])
		ODRecord[o_index][d_index][rent_peroid] += 1
		Total_ODRecord[o_index][rent_peroid] += 1
	inFile.close()
#1hr ver calculate
ODRecord_1hr = list()
for O in range(0,164):
	O_List = list()
	for D in range(0,164):
		D_List = list()
		for peroid in range(0,96):
			Record = 0
			D_List.append(Record)
		O_List.append(D_List)
	ODRecord_1hr.append(O_List)	

Total_ODRecord_1hr = list()
for O in range(0,164):
	O_List = list()
	for peroid in range(0,96):
		Total_Record = 0
		O_List.append(Total_Record)
	Total_ODRecord_1hr.append(O_List)	
	
	
for peroid in range(0,96,4):
	for O in range(0,164):
		Total_ODRecord_1hr[O][int(peroid/4)] = Total_ODRecord[O][peroid] + Total_ODRecord[O][peroid+1] + Total_ODRecord[O][peroid+2] + Total_ODRecord[O][peroid+3]
		for D in range(0,164):
			ODRecord_1hr[O][D][int(peroid/4)] = ODRecord[O][D][peroid] + ODRecord[O][D][peroid+1] + ODRecord[O][D][peroid+2] + ODRecord[O][D][peroid+3]
	
	
os.chdir('C:/Users/SyuShengWei/Desktop/project/')
if not os.path.exists('ODR_Peroid_15min'):
	os.makedirs('ODR_Peroid_15min')
os.chdir('C:/Users/SyuShengWei/Desktop/project/ODR_Peroid_15min')

for peroid in range(0,96):
	outFile = open(str(peroid).rjust(2,'0')+'.txt','a')
	for O in range(0,164):
		for D in range(0,164):
			ODR = round(ODRecord[O][D][peroid] / Total_ODRecord[O][peroid],5)
			outFile.write( str(ODR).ljust(6,'0') )
			if D == 163 :
				outFile.write('\n')
			else :
				outFile.write(' ')
	outFile.close()
	
os.chdir('C:/Users/SyuShengWei/Desktop/project/')
if not os.path.exists('ODR_Peroid_1HR'):
	os.makedirs('ODR_Peroid_1HR')
os.chdir('C:/Users/SyuShengWei/Desktop/project/ODR_Peroid_1HR')

for peroid in range(0,24):
	outFile = open(str(peroid).rjust(2,'0')+'.txt','a')
	for O in range(0,164):
		for D in range(0,164):
			ODR = round(ODRecord_1hr[O][D][peroid] / Total_ODRecord_1hr[O][peroid],5)
			outFile.write( str(ODR).ljust(6,'0') )
			if D == 163 :
				outFile.write('\n')
			else :
				outFile.write(' ')
	outFile.close()
