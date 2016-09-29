import os 

UVData = list()
for day in range(0,365):
	dayData = list()
	UVData.append(dayData)

os.chdir('C:/Users/SyuShengWei/Desktop/project')
inFile = open('AirData.csv','r')
titleLine = inFile.readline()
DataList = inFile.readlines()
day_index = 0
for theLine in DataList:
	if 'UVB' in theLine:
		theLine = theLine.strip('\n')
		lineInfo = theLine.split(',')
		for element in range(3,27):
			UVData[day_index].append(lineInfo[element])
		day_index += 1
			
print(UVData[])