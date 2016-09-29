'''
This program is use to produce data for Random Forest Predict
The data form is : 1.日期 2.時段 3.星期 4.平日或假日 5.天氣 6.Y(租借數量)
'''

import os 
import math
import calendar
#create 2D array to store StationInfomation
StationDic = {}
inFile = open('C:/Users/SyuShengWei/Desktop/project/stationInfomation/StationInfomation.txt','r')
titleLine = inFile.readline()
while True :
	theLine = inFile.readline()
	if theLine == '' :break
	else:
		stationInfo = theLine.split(',')
		if ' ' in stationInfo[0]:
			stationInfo[0] = stationInfo[0].strip(' ')
		new_dic = {stationInfo[1]:stationInfo[0]} # {stationName : number}
		StationDic.update(new_dic)
inFile.close()

#create a Dic to store [daynumber:Date]
DateDic = {}
dateCtr = 0
for filename in os.listdir('C:/Users/SyuShengWei/Desktop/project/RegularSplitByStation/000-捷運台北101(世貿站)'):
	date = filename.strip('.csv')
	new_dic = {dateCtr:date}
	DateDic.update(new_dic)
	dateCtr += 1
	
DateIndexDic = {}
dateCtr = 0
for filename in os.listdir('C:/Users/SyuShengWei/Desktop/project/RegularSplitByStation/000-捷運台北101(世貿站)'):
	date = filename.strip('.csv')
	new_dic = {date:dateCtr}
	DateIndexDic.update(new_dic)
	dateCtr += 1
 

#create a Dic to store week day e.g:[1:一]
WeekDayDic = {}
mon_dic 	= {'1':'一'}
tues_dic 	= {'2':'二'}
wednes_dic 	= {'3':'三'}
thurs_dic 	= {'4':'四'}
fri_dic 	= {'5':'五'}
satur_dic 	= {'6':'六'}
sun_dic 	= {'7':'日'}
WeekDayDic.update(mon_dic)
WeekDayDic.update(tues_dic)
WeekDayDic.update(wednes_dic)
WeekDayDic.update(thurs_dic)
WeekDayDic.update(fri_dic)
WeekDayDic.update(satur_dic)
WeekDayDic.update(sun_dic)

#print(WeekDayDic)

#create 1D array to store Holiday data
HolidayList = list()
inFile = open('C:/Users/SyuShengWei/Desktop/project/holiday.txt','r')
while True :
	theLine = inFile.readline()
	if theLine =='' : break
	else : 
		HolidayList.append(theLine.strip('\n'))
inFile.close()

for dirname in os.listdir('C:/Users/SyuShengWei/Desktop/project/RegularSplitByStation'):
	#create a 2D (302 * [24 * 4]) list to store the arrival data 
	DataList =  list()
	for i in range(0,302,1):
		dayList = list()
		os.chdir('C:/Users/SyuShengWei/Desktop/project/WeatherData')
		weatherFile = open(DateDic[i]+'.csv','r')
		weatherTitle = weatherFile.readline()
		weatherList = list()
		while True :
			theLine = weatherFile.readline()
			if theLine == '' :break
			else :
				weatherList.append(theLine)
		for j in range(0,96,1):
			peroidList = list() #  1.日期 2.時段 3.星期 4.平日或假日 5.天氣 6.Y(租借數量)
			#1->index 0
			peroidList.append(DateDic[i]) 
			#2->index 1
			peroidList.append(j+1)				
			#3->index 2
			weekdayInfo = DateDic[i].split('-')
			rentWeekDay = calendar.weekday(int(weekdayInfo[0]),int(weekdayInfo[1]),int(weekdayInfo[2])) + 1
			peroidList.append(WeekDayDic[str(rentWeekDay)])	
			#4->index 3
			if DateDic[i] in HolidayList:
				peroidList.append('假日')	
			else :
				peroidList.append('平日')
			#5->index 4
			weatherPeroid = math.floor(j/4)
			weatherInfo = weatherList[weatherPeroid].split(',')
			if weatherInfo[2] == '0.0' :
				peroidList.append('晴')
			else :
				peroidList.append('雨')
			#6->index 5
			if weatherInfo[2] != 'T' :
				peroidList.append(weatherInfo[2])
			else :
				peroidList.append('0.0')
			#7->index 6
			
			peroidList.append(0)	
			dayList.append(peroidList)
		DataList.append(dayList)
	#print(DataList)
	
	#start to scan data in the dir
	os.chdir('C:/Users/SyuShengWei/Desktop/project/RegularSplitByStation/'+dirname)
	for filename in os.listdir('C:/Users/SyuShengWei/Desktop/project/RegularSplitByStation/'+dirname):
		inFile = open(filename,'r')
		titleLine = inFile.readline()
		while True :
			theLine = inFile.readline()
			if theLine == '' : break 
			else :
				lineInfo = theLine.split(',')
				rentDate = lineInfo[0]
				peroid = math.floor(int(lineInfo[1]) / 900)
				DataList[DateIndexDic[rentDate]][peroid][6] += 1
	#merge the info into a line to output		
	outList = list()
	for i in range(0,302,1):
		for j in range(0,96,1):
			outLine = DataList[i][j][0] + ',' + str(DataList[i][j][1]) + ',' + DataList[i][j][2] + ',' + DataList[i][j][3] + ',' + DataList[i][j][4] + ',' + DataList[i][j][5] + ',' + str(DataList[i][j][6]) + '\n'
			outList.append(outLine)
	#output
	os.chdir('C:/Users/SyuShengWei/Desktop/project')
	if not os.path.exists('DataForRF'):
		os.makedirs('DataForRF')
	os.chdir('C:/Users/SyuShengWei/Desktop/project/DataForRF')
	outFile = open(dirname[0:3]+'.csv','a+')
	outFile.write('Date,Peroid,Weekday,WeekdayOrHoliday,Weather,Precp,Y\n')
	for element in outList :
		outFile.write(element)
	