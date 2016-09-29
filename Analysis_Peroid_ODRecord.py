import os



'''
os.chdir('C:/Users/SyuShengWei/Desktop/project/')
#normal day List
Normal_Day_List = list()
inFile = open('NormalDay.txt','r')
Data_List = inFile.readlines()
for theLine in Data_List:
	Normal_Day_List.append(theLine.strip('\n'))
inFile.close()


ODR_Record_1HR = list()
for O in range(0,164):
	O_List = list()
	for D in range(0,164):
		D_List = list()
		for peroid in range(0,24):
			peroid_record = 0
			D_List.append(peroid_record)
		O_List.append(D_List)
	ODR_Record_1HR.append(O_List)

Total_ODRecord_1HR = list()	
for O in range(0,164):
	O_List = list()
	for peroid in range(0,24):
		peroid_record = 0
		O_List.append(peroid_record)
	Total_ODRecord_1HR.append(O_List)	
	
ODR_Record_30min = list()
for O in range(0,164):
	O_List = list()
	for D in range(0,164):
		D_List = list()
		for peroid in range(0,48):
			peroid_record = 0
			D_List.append(peroid_record)
		O_List.append(D_List)
	ODR_Record_30min.append(O_List)
	
Total_ODRecord_30min = list()	
for O in range(0,164):
	O_List = list()
	for peroid in range(0,48):
		peroid_record = 0
		O_List.append(peroid_record)
	Total_ODRecord_30min.append(O_List)

for filename in os.listdir('C:/Users/SyuShengWei/Desktop/project/RegularForm'):
	os.chdir('C:/Users/SyuShengWei/Desktop/project/RegularForm')
	the_day = filename.strip('.csv')
	if the_day not in Normal_Day_List : continue
	else:
		inFile = open(filename,'r')
		titelLine = inFile.readline()
		Data_List = inFile.readlines()
		for dataLine in Data_List:
			theLine = dataLine.strip('\n')
			Line_Info = theLine.split(',')
			o_index = int(Line_Info[4])
			d_index = int(Line_Info[5])
			peroid_index_1hr = int(Line_Info[1])//3600
			peroid_index_30min = int(Line_Info[1])//1800
			ODR_Record_1HR[o_index][d_index][peroid_index_1hr] 		+= 1
			ODR_Record_30min[o_index][d_index][peroid_index_30min] 	+= 1
			Total_ODRecord_1HR[o_index][peroid_index_1hr] 			+= 1
			Total_ODRecord_30min[o_index][peroid_index_30min] 		+= 1
		inFile.close()

os.chdir('C:/Users/SyuShengWei/Desktop/project/')
if not os.path.exists('ODR_Record'):
	os.makedirs('ODR_Record')
os.chdir('C:/Users/SyuShengWei/Desktop/project/ODR_Record')
'''




outFile = open('ODR_Record_1HR.txt','a') #O1D1,O1D2 .... : O2D1,O2D2 .... : '/n'(one peroid)
for peroid in range(0,24):
	for O in range(0,164):
		for D in range(0,164):
			outFile.write(str(ODR_Record_1HR[O][D][peroid]))
			if D != 163 :
				outFile.write(',')
			else:
				outFile.write(':')
	outFile.write('\n')
outFile.close()


outFile = open('ODR_Record_30min.txt','a')
for peroid in range(0,48):
	for O in range(0,164):
		for D in range(0,164):
			outFile.write(str(ODR_Record_30min[O][D][peroid]))
			if D != 163 :
				outFile.write(',')
			else:
				outFile.write(':')
	outFile.write('\n')
outFile.close()

outFile = open('Total_OD_1HR.txt','a')
for O in range(0,164):
	for peroid in range(0,24):
		outFile.write(str(Total_ODRecord_1HR[O][peroid]))
		if peroid != 23:
			outFile.write(',')
		else: 
			outFile.write('\n')
outFile.close()

outFile = open('Total_OD_30min.txt','a')
for O in range(0,164):
	for peroid in range(0,48):
		outFile.write(str(Total_ODRecord_30min[O][peroid]))
		if peroid != 47:
			outFile.write(',')
		else: 
			outFile.write('\n')
outFile.close()

