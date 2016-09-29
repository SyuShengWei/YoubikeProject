import os

StationList_164 = list()

os.chdir('C:/Users/SyuShengWei/Desktop/project/stationInfomation')
inFile = open('StationInfomation_ForRegular.txt','r')
titleLine = inFile.readline()
DataList = inFile.readlines()
for theLine in DataList:
	theLine = theLine.split(',')
	station = theLine[1]
	StationList_164.append(station)
inFile.close()
#print(StationList_164)

StationList_182 = list()
StationList_Dif = list()

os.chdir('C:/Users/SyuShengWei/Desktop/project/splitByDay/10')
for filename in os.listdir('C:/Users/SyuShengWei/Desktop/project/splitByDay/10'):
	os.chdir('C:/Users/SyuShengWei/Desktop/project/splitByDay/10')
	inFile = open(filename,'r')
	DataList = inFile.readlines()
	for theLine in DataList:
		theLine = theLine.split(',')
		station = theLine[2]
		if station not in StationList_182 :
			StationList_182.append(station)
		if station not in StationList_164 and station not in StationList_Dif:
			StationList_Dif.append(station)
	inFile.close()
	
os.chdir('C:/Users/SyuShengWei/Desktop/project')
outFile = open('StationList_182.txt','a')
for station in StationList_182:
	outFile.write(station+'\n')
outFile.close()

outFile = open('StationList_164.txt','a')
for station in StationList_164:
	outFile.write(station+'\n')
outFile.close()

outFile = open('StationList_Dif.txt','a')
for station in StationList_Dif:
	outFile.write(station+'\n')
outFile.close()