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



os.chdir('C:/Users/SyuShengWei/Desktop/project')
inFile = open('ODrate_check4type.txt')
theData = inFile.readlines()
for i in range(0,len(theData)):
	OIndex = int(i / 164)
	DIndex = i % 164
	theData[i] = theData[i].strip('\n')
	anODData = theData[i].split(',')
	for k in range(0,4):
		ODrateMatrix[OIndex][DIndex][k] = int(anODData[k])

for i in range(0,163):
	totalODList = [0,0,0,0]
	for j in range(0,163):
		for k in range(0,4):
			totalODList[k] += ODrateMatrix[i][j][k]	
	for j in range(0,163):
		for k in range(0,4):
			temp = ODrateMatrix[i][j][k]
			ODrateMatrix[i][j][k] = round(temp/totalODList[k],3)

outputList = list()
for i in range (0,164):
	for j in range (0,164):
		outLine = list()
		for k in range (0,4):
			outLine.append(ODrateMatrix[i][j][k])
		outputLine = str(outLine[0]).rjust(5) + ',' + str(outLine[1]).rjust(5) + ',' + str(outLine[2]).rjust(5) + ',' + str(outLine[3]).rjust(5) + '\n'
		outputList.append(outputLine)
	
os.chdir('C:/Users/SyuShengWei/Desktop/project')
outFile = open ('ODrate_compare.txt','a+')
outFile.write('沒雨、非假,下雨、非假,沒雨、假日,下雨、假日\n')
for element in outputList:
	outFile.write(element)
outFile.close()
