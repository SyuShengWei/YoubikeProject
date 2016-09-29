import os 

ODR_Record = list()
for O in range(0,164):
	O_List = list()
	for D in range(0,164):
		D_List = 0
		O_List.append(D_List)
	ODR_Record.append(O_List)

	
for filename in os.listdir('C:/Users/SyuShengWei/Desktop/project/RegularForm'):
	os.chdir('C:/Users/SyuShengWei/Desktop/project/RegularForm')
	inFile = open(filename,'r')
	titleLine = inFile.readline()
	Data_List = inFile.readlines()
	for dataLine in Data_List :
		theLine = dataLine.strip('\n')
		Line_Info = theLine.split(',')
		o_index = int(Line_Info[4])
		d_index = int(Line_Info[5])
		ODR_Record[o_index][d_index] += 1
	inFile.close()
	
Top10_Station = list()
Top10_Values  = list()
for O in range(0,164):
	O_List = list()
	O_Value= list()
	for i in range(0,10):
		O_List.append(-1)
		O_Value.append(-1)
	Top10_Station.append(O_List)
	Top10_Values.append(O_Value)

	
	
for O in range(0,164):
	for D in range(0,164):
		for index in range(0,10):
			if ODR_Record[O][D] >= Top10_Values[O][index] :
				Top10_Values[O].insert(index,ODR_Record[O][D])
				Top10_Station[O].insert(index,D)
				lose_value = Top10_Values[O].pop()
				lose_Station = Top10_Station[O].pop()
				break
			else:
				continue

	
outFile = open('C:/Users/SyuShengWei/Desktop/project/ODR_Top10.txt','a')
for O in range (0,164):
	print(Top10_Station[O])
	print(Top10_Values[O])
	for i in range(0,10):
		outFile.write(str(Top10_Station[O][i]))
		if i != 9:
			outFile.write(',')
		else:
			outFile.write('\n')