import os
ODrateMatrix = list()
for i in range (0,164):
	distinationList = list()
	for j in range(0,164):
		eachKindDataList = list()
		for k in range(0,4):
			totalOD = 0
			eachKindDataList.append(totalOD)
		distinationList.append(eachKindDataList)
	ODrateMatrix.append(distinationList)


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
	print(theDay)
	if theDay in OutlierList or theDay =='except':
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
	inFile = open(filename)
	titleLine = inFile.readline()
	while True:
		theLine = inFile.readline()
		if theLine == '' :
			break
		else :
			try:
				lineInfo = theLine.split(',')
				OIndex = int(lineInfo[4])
				DIndex = int(lineInfo[5])
				ODrateMatrix[OIndex][DIndex][dataKind] += 1	
			except :
				print(theLine)

outputList = list()
for i in range (0,164):
	for j in range (0,164):
		outLine = list()
		for k in range (0,4):
			outLine.append(ODrateMatrix[i][j][k])
		outputLine = str(outLine[0]) + ',' + str(outLine[1]) + ',' + str(outLine[2]) + ',' + str(outLine[3]) + '\n'
		outputList.append(outputLine)
		 
os.chdir('C:/Users/SyuShengWei/Desktop/project')
outFile = open ('ODrateFile.txt','a+')
for element in outputList:
	outFile.write(element)
outFile.close()

