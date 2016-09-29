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


SameStationList = list()

for StationName in os.listdir('C:/Users/SyuShengWei/Desktop/project/RegularSplitByStation'):
	'''
	#生成需要資料

	ODRecord = list() #[day][D][peroid]
	for day in range(0,len(NormalDay)):
		dayList = list()
		for distination in range(0,164):
			DList = list()
			for peroid in range(0,(24*4)):
				peroidList = 0
				DList.append(peroidList)
			dayList.append(DList)
		ODRecord.append(dayList)

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


	Total_OD = 0
	DayTotalOD = list()
	for filename in os.listdir('C:/Users/SyuShengWei/Desktop/project/RegularSplitByStation/'+StationName):
		totalOD = 0
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
				Total_OD += 1 
				totalOD +=1
				ODRecord[DayIndex][DIndex][PeroidIndex] += 1
				TravelTimeRecord[DayIndex][DIndex][PeroidIndex].append(TravelTime)
			DayTotalOD.append(totalOD)
	os.chdir('C:/Users/SyuShengWei/Desktop/project/Analysis/'+StationName)

#each line record a OD's day OD num
	outFile = open('ODRecord.txt','a')
	outFile.write(str(Total_OD) + '\n')
	for OD in range(0,len(DayTotalOD)):
		outFile.write(str(DayTotalOD[OD]))
		if OD != (len(DayTotalOD) - 1) :
			outFile.write(',')
		else:
			outFile.write('\n')
	for day in range(0,len(NormalDay)):
		for distination in range(0,164):
			for peroid in range(0,(24*4)):
				outFile.write(str(ODRecord[day][distination][peroid]))
				if peroid != 95 :
					outFile.write(',')
			outFile.write('\n')

	outFile.close()

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
	ODRecord = list() #[day][D][peroid]
	for day in range(0,len(NormalDay)):
		dayList = list()
		for distination in range(0,164):
			DList = list()
			for peroid in range(0,(24*4)):
				peroidList = 0
				DList.append(peroidList)
			dayList.append(DList)
		ODRecord.append(dayList)

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
	'''
		
	os.chdir('C:/Users/SyuShengWei/Desktop/project/Analysis/'+StationName)
	inFile = open('ODRecord.txt','r')
	TotalOD = int(inFile.readline().strip('\n'))
	DayTotalOD = inFile.readline().strip('\n').split(',')
	DataList = inFile.readlines()

	for lineIndex in range(0,len(DataList)):
		theLine = DataList[lineIndex].strip('\n')
		temp_oneDayOD = theLine.split(',')
		oneDayOD = list()
		for temp_element in temp_oneDayOD :
			element = int(temp_element)
			oneDayOD.append(element)
		ODRecord[int(lineIndex/164)][lineIndex%164] = oneDayOD
	inFile.close()
	
	'''
	inFile = open('TravelRecord.txt')
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
	'''
	

	#1.針對一整天的OD，個時段是否相同 ->加總每天(98)天，比較各時段
	#2.針對同時段的OD，每天是否相同	 ->加總同時段(96)，比較各天
	
	PeroidCompareList = list()
	for distination in range(0,164):
		DList = list()
		for peroid in range(0,96):
			PeroidList = 0
			DList.append(PeroidList)
		PeroidCompareList.append(DList)

	PeroidCompareTotal = list()
	for peroid in range(0,96):
		PeroidCompareTotal.append(0)

	DayCompareList = list()	
	for day in range(0,len(NormalDay)):
		dayList = list()
		for distination in range(0,164):
			DList = 0
			dayList.append(DList)
		DayCompareList.append(dayList)

	DayCompareTotal = list()
	for day in range(0,len(NormalDay)):
		DayCompareTotal.append(0)	

	for day in range(0,len(NormalDay)):
		for distination in range(0,164):
			for peroid in range(0,96):
				PeroidCompareList[distination][peroid] += ODRecord[day][distination][peroid]
				DayCompareList[day][distination] += ODRecord[day][distination][peroid]
				#print (type(ODRecord[day][distination][peroid]))
				PeroidCompareTotal[peroid] += ODRecord[day][distination][peroid]
				DayCompareTotal[day] += ODRecord[day][distination][peroid]

#print (DayCompareTotal[0] == sum(DayCompareList[0]))
#print (PeroidCompareTotal[0] == total)

#
#output every od rate i need
#
	'''
	outFile = open('PeroidCompareList.csv','a')
	for peroid in range(0,96):
		for distination in range(0,164):
			if PeroidCompareTotal[peroid] != 0 :
				outFile.write(str(round(PeroidCompareList[distination][peroid]/PeroidCompareTotal[peroid],3)).rjust(4,' '))
			else :
				outFile.write(str(0).rjust(4,' '))
			if distination  != 163 :
				outFile.write(',')
			else :
				outFile.write('\n')
	outFile.close()

	outFile = open('DayCompareList.csv','a')
	for day in range(0,len(NormalDay)):
		for distination in range(0,164):
			if DayCompareTotal[day] !=0 :
				outFile.write(str(round(DayCompareList[day][distination]/DayCompareTotal[day],3)).rjust(5,' '))
			else:
				outFile.write(str(0).rjust(5,' '))
			if distination != 163 :
				outFile.write(',')
			else :
				outFile.write('\n')
	outFile.close()
	'''
#
#
#


#
#前10名站
#
	PeroidCompareRateList = list()
	for peroid in range(0,96):
		PeroidList = list()
		for distination in range(0,164):
			if PeroidCompareTotal[peroid] != 0 :
				DList = round(PeroidCompareList[distination][peroid]/PeroidCompareTotal[peroid],5)
			else :
				DList = 0
			PeroidList.append(DList)
		PeroidCompareRateList.append(PeroidList)

#print(PeroidCompareRateList[0])


	Top10_Peroid = list()
	for peroid in range(0,96):
		PeroidList = list()
		for distination in range(0,164):
			DList = 0
			PeroidList.append(DList)
		Top10_Peroid.append(PeroidList)
	
	
	
	Top10_Peroid_Staton = list ()
	for peroid in range(0,96):
		PeroidList = list()
		for distination in range(0,164):
			DList = -1
			PeroidList.append(DList)
		Top10_Peroid.append(PeroidList)
	
	
	DayCompareRateList = list()	
	for day in range(0,len(NormalDay)):
		dayList = list()
		for distination in range(0,164):
			if DayCompareTotal[day] != 0:
				DList = round(DayCompareList[day][distination]/DayCompareTotal[day],5)
			else:
				DList = 0
			dayList.append(DList)
		DayCompareRateList.append(dayList)	
	
	Top10_Day = list()	
	for day in range(0,len(NormalDay)):
		dayList = list()
		for distination in range(0,10):
			DList = 0
			dayList.append(DList)
		Top10_Day.append(dayList)
	
	Top10_Day_Staton = list()	
	for day in range(0,len(NormalDay)):
		dayList = list()
		for distination in range(0,10):
			DList = -1
			dayList.append(DList)
		Top10_Day_Staton.append(dayList)

	for peroid in range(0,96):
		for destination in range(0,164):
			for index in range(0,10):
				if PeroidCompareRateList[peroid][destination] >= Top10_Day[peroid][index] :
					Top10_Day[peroid].insert(index,str(PeroidCompareRateList[peroid][destination]))
					Top10_Day[peroid][index] = float(Top10_Day[peroid][index])
					Top10_Day_Staton[peroid].insert(index,destination)
					losing = Top10_Day[peroid].pop(10)
					losing_Station = Top10_Day_Staton[peroid].pop(10)
					break
				else :
					continue


#print(Top10_Day[1])
	'''
	outFile = open('Top10_Peroid.txt','a')
	for	peroid in range(0,96):
		outFile.write(str(peroid).rjust(2,' ') + ',' + str(peroid//4).rjust(2,'0') + ' : ')
		for index in range(0,10):
			outFile.write(str(Top10_Day_Staton[peroid][index]).rjust(3,'0'))
			outFile.write(' , ')
		for index in range(0,10):	
			outFile.write(str(Top10_Day[peroid][index]).ljust(8,'0'))
			if index != 9 : 
				outFile.write(' , ')
			else :
				outFile.write('\n')
	'''

#畫圖Top10_Peroid_1

	TopList = list()
	MostList = list()
	for D in range(0,164):
		MostList.append(0)

	for peroid in range(0,96):
		MostList[int(Top10_Day_Staton[peroid][0])] +=1

	Mostnum = max(MostList)
	MostStation = int(MostList.index(Mostnum))

	'''
	outFile = open('Top10_Peroid_1.txt','a')
	for peroid in range(0,96):
		if Top10_Day_Staton[peroid][0] != MostStation : continue
		else :
			outFile.write(str(peroid).rjust(2,' ') + ',' + str(peroid//4).rjust(2,'0') + ' : ')
			for index in range(0,10):
				outFile.write(str(Top10_Day_Staton[peroid][index]).rjust(3,'0'))
				outFile.write(' , ')
			for index in range(0,10):	
				outFile.write(str(Top10_Day[peroid][index]).ljust(8,'0'))
				if index != 9 : 
					outFile.write(' , ')
				else :
					outFile.write('\n')
	'''
	for peroid in range(0,96):
		if Top10_Day_Staton[peroid][0] != MostStation : continue
		else :
			TopList.append(Top10_Day[peroid][0])				

				
	'''
	#top 10 出現最多次
	x = np.arange(0,len(TopList))
	y = TopList
	fig = plt.figure()
	ax = fig.add_subplot(111)
	t = ax.plot(x,y,'ro')
	t = ax.plot(x,y)
	fig.savefig('Top1_Probability.png')
	plt.close(fig)
	
	Top1List = list()
	for peroid in range(0,96):
		Top1List.append(Top10_Day[peroid][0])
	x = np.arange(0,len(Top1List))
	y = Top1List
	fig = plt.figure()
	ax = fig.add_subplot(111)
	t = ax.plot(x,y,'ro')
	t = ax.plot(x,y)
	fig.savefig('Top1_ALL_Probability.png')
	plt.close(fig)
	
	TopNumList = list()
	for peroid in range(0,96):
		if Top10_Day_Staton[peroid][0] != MostStation : continue
		else :
			TopNumList.append(PeroidCompareList[MostStation][peroid])				
	
	x = np.arange(0,len(TopNumList))
	y = TopNumList
	fig = plt.figure()
	ax = fig.add_subplot(111)
	t = ax.plot(x,y,'ro')
	t = ax.plot(x,y)
	fig.savefig('Top1_Num.png')
	plt.close(fig)
	
	'''
	'''
	Top10NumList = list()
	for peroid in range(0,96):
		Top10NumList.append(PeroidCompareList[Top10_Day_Staton[peroid][0]][peroid])				
	
	x = np.arange(0,len(Top10NumList))
	y = Top10NumList
	fig = plt.figure()
	ax = fig.add_subplot(111)
	t = ax.plot(x,y,'ro')
	t = ax.plot(x,y)
	fig.savefig('Top10NumList.png')
	plt.close(fig)
	'''
	
	try:
		StationNow = int(StationName[0:3])
		if MostStation == StationNow:
			SameStationList.append(StationNow)
	except:
		print('same Station error')
	print(StationNow,end = ' ')
	print(SameStationList)
	
#
#
#

os.chdir('C:/Users/SyuShengWei/Desktop/project/Analysis')
outFile = open('SameStation.txt','a')
for station in SameStationList:
	outFile.write(str(station) + '\n')
outFile.close()