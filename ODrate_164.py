import os

NormalDay = list()
os.chdir('C:/Users/SyuShengWei/Desktop/project')
inFile = open('NormalDay.txt','r')
DataList = inFile.readlines()
for theLine in DataList:
	theLine = theLine.strip('\n')
	NormalDay.append(theLine)

ODRMatrix = list()
for O in range(0,164):
	OList = list()
	for D in range(0,164):
		DList = 0
		OList.append(DList)
	ODRMatrix.append(OList)
	
ODtotal = list()
for O in range(0,164):
	ODtotal.append(0)

for filename in os.listdir('C:/Users/SyuShengWei/Desktop/project/RegularForm'):
	os.chdir('C:/Users/SyuShengWei/Desktop/project/RegularForm')
	inFile = open(filename,'r')
	titleLine = inFile.readline()
	DataList = inFile.readlines()
	for theLine in DataList :
		theLine = theLine.split(',')
		OIndex = int(theLine[4])
		DIndex = int(theLine[5])
		ODRMatrix[OIndex][DIndex] += 1
		ODtotal[OIndex] += 1

os.chdir('C:/Users/SyuShengWei/Desktop/project')

outFile = open('ODrate_num.txt','a')
for O in range(0,164):
	outFile.write(str(ODtotal[O]))
	if O != 163:
		outFile.write(' ')
	else :
		outFile.write('\n')
for O in range(0,164):
	for D in range(0,164):
		outFile.write(str(ODRMatrix[O][D]))
		if D != 163:
			outFile.write(' ')
		else :
			outFile.write('\n')
outFile.close()
