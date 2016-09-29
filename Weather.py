import os 
import codecs

'''
data form  1. start time (0) 2. end time (1) 3. how much rain (11)
'''
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



whichFile = 1

UVDay = 0
os.chdir('C:/Users/SyuShengWei/Desktop/project/weather/2014')
for filename in os.listdir('C:/Users/SyuShengWei/Desktop/project/weather/2014'):
	os.chdir('C:/Users/SyuShengWei/Desktop/project/weather/2014')
	print('File is : '+ str(whichFile) )
	dataLineList = list()
	inFile = codecs.open(filename,'r','UTF-8')
	theLine = inFile.readline()
	ctr = 0
	UVHour =0
	while True :
		dataElementList = list()
		theLine = inFile.readline()
		if theLine == '' : break
		else :
			ctr += 1
			lineInfo = theLine.split(',')
			#時段
			timeStart 	= int(lineInfo[0]) *60 *60
			timeEnd 	= int(lineInfo[1])	*60 *60
			dataElementList.append(str(timeStart))
			dataElementList.append(str(timeEnd))
			#雨量
			tempInfo11 = lineInfo[11][0:len(lineInfo[11])-1]
			lineInfo[11] = tempInfo11
			dataElementList.append(lineInfo[11])
			#下雨小時
			tempInfo12 = lineInfo[12][0:3]
			lineInfo[12] = tempInfo12
			dataElementList.append(lineInfo[12])
			#氣溫
			tempInfo4 = lineInfo[4][0:-1]
			lineInfo[4] = tempInfo4
			dataElementList.append(lineInfo[4])
			#UVB
			dataElementList.append(UVData[UVDay][UVHour])
			
			dataLine = dataElementList[0] + ',' + dataElementList[1] + ',' + dataElementList[2] + ',' + dataElementList[3] + ',' + dataElementList[4] + ',' + dataElementList[5]
			dataLineList.append(dataLine)
			UVHour += 1
	#print(dataLineList)
	if ctr != 24 :
		print('error file = ' + str(whichFile) + ' with line : ' + str(ctr) )
	
	os.chdir('C:/Users/SyuShengWei/Desktop/project')
	if not os.path.exists('WeatherDataWithTemperature'):
		os.makedirs('WeatherDataWithTemperature')
	os.chdir('C:/Users/SyuShengWei/Desktop/project/WeatherDataWithTemperature')
	
	outFile = open(filename,'a+')
	outFile.write('StartTime,EndTime,Precp(mm),PrecpHour(hr),Tempture(C),UVB \n ')
	for element in dataLineList :
		outFile.write(str(element))
		outFile.write('\n')
	outFile.close()
	whichFile += 1
	UVDay += 1
	
