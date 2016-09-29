import os 

OutputList = list()

rainDayList = list()

fileCtr = 1
for filename in os.listdir('C:/Users/SyuShengWei/Desktop/project/WeatherData'):
	os.chdir('C:/Users/SyuShengWei/Desktop/project/WeatherData')
	inFile = open(filename,'r')
	titleLine = inFile.readline()
	
	total_rain_time  = 0.0
	total_rain_precp = 0.0
	how_many_T		 = 0
	
	while True : 
		theLine = inFile.readline()
		if theLine == '' : break
		else :
			lineInfo = theLine.split(',')
			if lineInfo[2] == 'T' :
				total_rain_precp = total_rain_precp + 0.05
				how_many_T = how_many_T + 1
			else :
				total_rain_precp += float(lineInfo[2])
			total_rain_time += float(lineInfo[3])
	
	inFile.close()
	if total_rain_precp != 0.0 or total_rain_time != 0.0 :
		rainDayList.append(filename.strip('.csv')+'\n')
	
	outLine = filename.strip('.csv') + ',' + str(fileCtr) + ',' + str(round(total_rain_precp,2)) + ',' + str(round(total_rain_time,2)) + ',' + str(how_many_T) + '\n'
	OutputList.append(outLine)
	
	fileCtr += 1
	

os.chdir('C:/Users/SyuShengWei/Desktop/project')
outFile = open('WeatherTime.txt','a+')
outFile.write('Date,DayNum,Precp,Time,T\n')
for element in OutputList :
	outFile.write(element)
outFile.close()

outFile = open('RainDay.txt','a+')
for element in rainDayList :
	outFile.write(element)
outFile.close()
