#WeatherData have 24 WeatherDataLine which is store in dataList

class WeatherData :

	def __init__(self,dataList) :
		self.dataList = dataList
	
	def getList (self):
		return self.dataList
class WeatherDataLine :
	
	def __init__(self,startTime,endTime,precp,precpTime):
		self.startTime = startTime
		self.endTime = endTime
		self.precp = precp
		self.precpTime = precpTime

import os 
import codecs 
import calendar #use to return weekday -> 0~6 = mon,tuues,wednes,thurs,fir,satur,sun 

#create 1D array to store the except data 
exceptList = list()

#create 2D array to store StationInfomation
StationDic = {}
inFile = open('C:/Users/SyuShengWei/Desktop/project/stationInfomation/StationInfomation_ForRegular.txt','r')
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

#create 1D array to store Holiday data
HolidayList = list()
inFile = open('C:/Users/SyuShengWei/Desktop/project/holiday.txt','r')
while True :
	theLine = inFile.readline()
	if theLine =='' : break
	else : 
		HolidayList.append(theLine.strip('\n'))
inFile.close()

#create Dictionary to store WeatherData
WeatherDic = {}

for filename in os.listdir('C:/Users/SyuShengWei/Desktop/project/WeatherData'):
	dataList = list()
	
	inFile = open('C:/Users/SyuShengWei/Desktop/project/WeatherData/'+filename,'r')
	titleLine = inFile.readline()
	while True :
		theLine = inFile.readline()
		if theLine == '' : break
		else:
			lineInfo = theLine.split(',')
			if ' ' in lineInfo[0]:
				lineInfo[0].strip(' ')
				
			dataLine = WeatherDataLine(lineInfo[0],lineInfo[1],lineInfo[2],lineInfo[3])
			dataList.append(dataLine)
	weatherData = WeatherData(dataList)
	new_dic = {filename:weatherData}
	WeatherDic.update(new_dic)

#How to use weatherDic	
'''
weather = WeatherDic['2014-01-01.csv']
#print(weather.dataList[0].endTime)

for element in weather.dataList :
	print(element.endTime)
'''


#open the clean open data and record the form I want
#the data order is 1. rent date 2014-OO-XX 		2. rent time (in second) 
#				   3. return date 2014-OO-XX 	4. return time (in second)
#				   5. rent station (O)     		6. return station (D)
#				   7. week day (sun 7, mon 1 ....)	8. Holiday ? (T->1/F->0)
#				   9. rain ?(T/F)				10.how much rain (mm)
#				   11.travelTime(in second)
for filename in os.listdir('C:/Users/SyuShengWei/Desktop/project/SplitByDay(2014-OO-XX)'):
	
	outFileInfo = list()
	os.chdir('C:/Users/SyuShengWei/Desktop/project/SplitByDay(2014-OO-XX)')
	print('theFile =' + filename)
	inFile = open(filename,'r')
	while True :
		theLine = inFile.readline()
		if theLine == '' : break
		else :
			lineInfo = theLine.split(',')
			#rent
			rentInfo = lineInfo[1].split(' ')
			#1.rentDate
			if '2014-' in rentInfo[0] :
				rentDate = rentInfo[0]
				rentInfoSplit = rentInfo[0].split('-')
				rentWeekDay = calendar.weekday(int(rentInfoSplit[0]),int(rentInfoSplit[1]),int(rentInfoSplit[2])) + 1
			elif '2014/' in rentInfo[0]:
				rentInfoSplit = rentInfo[0].split('/')
				rentWeekDay = calendar.weekday(int(rentInfoSplit[0]),int(rentInfoSplit[1]),int(rentInfoSplit[2])) + 1
				if len(rentInfoSplit[1]) == 1 and len(rentInfoSplit[2]) == 1 :
					rentDate = rentInfoSplit[0] + '-0' + rentInfoSplit[1] + '-0' + rentInfoSplit[2]
				elif len(rentInfoSplit[1]) == 2 and len(rentInfoSplit) == 1 :
					rentDate = rentInfoSplit[0] + '-' + rentInfoSplit[1] + '-0' + rentInfoSplit[2]
				elif len(rentInfoSplit[1]) == 1 and len(rentInfoSplit) == 2 :
					rentDate = rentInfoSplit[0] + '-0' + rentInfoSplit[1] + '-' + rentInfoSplit[2] 
				elif len(rentInfoSplit[1]) == 2 and len(rentInfoSplit) == 2 :
					rentDate = rentInfoSplit[0] + '-' + rentInfoSplit[1] + '-' + rentInfoSplit[2]
				else :
					exceptList.append(theLine)
					continue
			else :
				exceptList.appned(theLine)
				continue
			#2.rentTime
			rentTimeInfo = rentInfo[1].split(':')
			rentTime =  int(rentTimeInfo[0][0:2])*60*60 + int(rentTimeInfo[1][0:2])*60 + int(rentTimeInfo[2][0:2]) 			
			#return 
			#3.returnDate
			returnInfo = lineInfo[3].split(' ')
			if '2014-' in returnInfo[0] :
				returnDate = returnInfo[0]
				returnInfoSplit = returnInfo[0].split('-')
				returnWeekDay = calendar.weekday(int(returnInfoSplit[0]),int(returnInfoSplit[1]),int(returnInfoSplit[2])) + 1
			elif '2014/' in returnInfo[0] :
				returnInfoSplit = returnInfo[0].split('/')
				returnWeekDay = calendar.weekday(int(returnInfoSplit[0]),int(returnInfoSplit[1]),int(returnInfoSplit[2])) + 1
				if len(returnInfoSplit[1]) == 1 and len(returnInfoSplit[2]) == 1 :
					returnDate = returnInfoSplit[0] + '-0' + returnInfoSplit[1] + '-0' + returnInfoSplit[2]
				elif len(returnInfoSplit[1]) == 2 and len(returnInfoSplit[2]) == 1 :
					returnDate = returnInfoSplit[0] + '-' + returnInfoSplit[1] + '-0' + returnInfoSplit[2]
				elif len(returnInfoSplit[1]) == 1 and len(returnInfoSplit[2]) == 2 :
					returnDate = returnInfoSplit[0] + '-0' + returnInfoSplit[1] + '-' + returnInfoSplit[2]
				elif len(returnInfoSplit[1]) == 2 and len(returnInfoSplit[2]) == 2 :
					returnDate = returnInfoSplit[0] + '-' + returnInfoSplit[1] + '-' + returnInfoSplit[2]
				else :
					exceptList.append(theLine)
					continue
			else: 
				continue
			
			#4.returnTime
			returnTimeInfo = returnInfo[1].split(':')
			returnTime =  int(returnTimeInfo[0][0:2])*60*60 + int(returnTimeInfo[1][0:2])*60 + int(returnTimeInfo[2][0:2]) 
			
			#5.rentStation
			
			try	:
				rentStation = StationDic[lineInfo[2]]
			except :
				exceptList.append(theLine)
				print(theLine)
				continue
			
			#6.returnStation
			try	:
				returnStation = StationDic[lineInfo[4]]
			except :
				exceptList.append(theLine)
				print(theLine)
				continue
			
			
			#7.rentWeekDay -->done at  1.
			
			#8.holiday ? 
			if rentDate in HolidayList :
				rentHoliday = '1'
			else :
				rentHoliday = '0'
				
			#9rain? 10how much
			weather = WeatherDic[filename]
			for element in weather.dataList :
				if rentTime in range(int(element.startTime),int(element.endTime)):
					if element.precp == '0.0' :   
						rain = '0'
						precpMM = '0.0'
					elif element.precp == 'T':
						rain = '0'
						precpMM = element.precp
					else :
						rain = '1'
						precpMM = element.precp
			#11.travelTime
			travleTimeInfo = lineInfo[5].split(':')
			travelTime =  int(travleTimeInfo[0][0:2])*60*60 + int(travleTimeInfo[1][0:2])*60 + int(travleTimeInfo[2][0:2])
			
			#merge data
			theInfoLine = rentDate + ',' +	str(rentTime) + ',' + returnDate + ',' + str(returnTime) + ',' + rentStation + ',' + returnStation + ',' + str(rentWeekDay) + ',' + rentHoliday + ',' + rain + ',' + precpMM + ',' +str(travelTime)		
			#print(theInfoLine)
			outFileInfo.append(theInfoLine)
	inFile.close()
	os.chdir('C:/Users/SyuShengWei/Desktop/project')
	if not os.path.exists('RegularForm_UpdateRainT'):
		os.makedirs('RegularForm_UpdateRainT')
	os.chdir('C:/Users/SyuShengWei/Desktop/project/RegularForm_UpdateRainT')
	outFile = open(filename,'a+')
	outFile.write('rent date,rent time,return date,return time,rent station (O),return station (D),week day,Holiday,Rain,precp(mm),travelTime')
	outFile.write('\n')
	for element in outFileInfo:
		outFile.write(element)
		outFile.write('\n')
	outFile.close()


os.chdir('C:/Users/SyuShengWei/Desktop/project/RegularForm_UpdateRainT')
outFile = open('except.csv','a+')
for element in exceptList :
	outFile.write(element)
	outFile.write('\n')
outFile.close()