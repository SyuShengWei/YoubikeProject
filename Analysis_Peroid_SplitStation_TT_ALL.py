import os 
import numpy as np
import matplotlib.pyplot as plt

os.chdir('C:/Users/SyuShengWei/Desktop/project')

NormalDay = list()

inFile = open('NormalDay.txt','r')
Data = inFile.readlines()
for theLine in Data :
	theLine = theLine.strip('\n')
	NormalDay.append(theLine)
inFile.close()

for StationName in os.listdir('C:/Users/SyuShengWei/Desktop/project/RegularSplitByStation'):
	#產生
	'''
	TravelTimeRecord = list() #[day][d][peroid][travelData]
	for day in range(0,len(NormalDay)):
		dayList = list()
		for distination in range(0,164):
			DList = list()
			for peroid in range(0,(24*4)):
				peroidList = list()
				DList.append(peroidList)
			dayList.append(DList)
		TravelTimeRecord.append(dayList)
		
	for filename in os.listdir('C:/Users/SyuShengWei/Desktop/project/RegularSplitByStation/'+StationName):
		os.chdir('C:/Users/SyuShengWei/Desktop/project/RegularSplitByStation/'+StationName)
		theDay = filename.strip('.csv')
		if theDay not in NormalDay :
			continue
		else:	
			inFile = open(filename,'r')
			titleLine = inFile.readline()
			DataList = inFile.readlines()
			for theLine in DataList :
				theLine = theLine.strip('\n')
				lineInfo = theLine.split(',')
				DayIndex = NormalDay.index(theDay)
				DIndex = int(lineInfo[5])
				PeroidIndex = int(int(lineInfo[1])/900)
				TravelTime = int(lineInfo[10])
				TravelTimeRecord[DayIndex][DIndex][PeroidIndex].append(TravelTime)
	os.chdir('C:/Users/SyuShengWei/Desktop/project/Analysis/'+StationName)
	
	#each line record a OD's peroid travel data
	outFile = open('TravelRecord.txt','a')
	for day in range(0,len(NormalDay)):
		for distination in range(0,164):
			for peroid in range(0,(24*4)):
				if len(TravelTimeRecord[day][distination][peroid]) == 0 :
					outFile.write(str(0))
				else:
					for data in range(len(TravelTimeRecord[day][distination][peroid])):
						outFile.write(str(TravelTimeRecord[day][distination][peroid][data]))
						if data != (len(TravelTimeRecord[day][distination][peroid]) -1) :
							outFile.write(',')
				outFile.write('\n')
	outFile.close()
	'''
	#讀取
	
	
	os.chdir('C:/Users/SyuShengWei/Desktop/project/Analysis/'+StationName)
	inFile = open('TravelRecord.txt','r')
	DataList = inFile.readlines()
	for lineIndex in range(0,len(DataList)):
		#每96行 1天 OD
		#每96*164行  每OD的每天
		theLine = DataList[lineIndex].strip('\n')
		if theLine == '0' : continue
		else : 
			onePeroid = theLine.split(',')
			for element in onePeroid :
				element = int(element)
			TravelTimeRecord[int(lineIndex/(96*164))][int(lineIndex/96)%164][lineIndex%96] = onePeroid
	
	break