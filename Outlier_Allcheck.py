import os
import numpy as np
import matplotlib.pyplot as plt
import Outlier as OL
#test
std_range = float(input('Enter the STD range :'))
#read File
TravelList = list()

inFile = open('C:/Users/SyuShengWei/Desktop/project/TotalTravelOfSystem.txt','r')
titleLine = inFile.readline()
while True :
	theLine = inFile.readline()
	if theLine == '': break 
	else :
		lineInfo = theLine.split(',')
		TravelList.append(int(lineInfo[2].strip('\n')))
#start to check

TravelList_2 = list()
TravelList_3 = list()

outlierData_1 = OL.outlier(TravelList,std_range)

for i in range (0,len(TravelList)):
	if i not in outlierData_1[0] and i not in outlierData_1[1]:
		TravelList_2.append(TravelList[i])

outlierData_2 = OL.outlier(TravelList,float(std_range),TravelList_2)
for i in range (0,len(TravelList)):
	if i not in outlierData_2[0] and i not in outlierData_2[1]:
		TravelList_3.append(TravelList[i])

outlierData_3 = OL.outlier(TravelList,float(std_range),TravelList_3)

OutputList = list()
rainDayList = list()

fileCtr = 1
for filename in os.listdir('C:/Users/SyuShengWei/Desktop/project/WeatherData'):
	os.chdir('C:/Users/SyuShengWei/Desktop/project/WeatherData')
	inFile = open(filename,'r')
	titleLine = inFile.readline()
	
	total_rain_time  = 0
	total_rain_precp = 0
	how_many_T		 = 0
	
	while True : 
		theLine = inFile.readline()
		if theLine == '' : break
		else :
			lineInfo = theLine.split(',')
			if lineInfo[2] == 'T' :
				total_rain_precp += 0.05
				how_many_T += 1
			else :
				total_rain_precp += float(lineInfo[2])
			total_rain_time  += float(lineInfo[3])
	inFile.close()
	if total_rain_precp != 0.0 or total_rain_time != 0.0 :
		rainDayList.append(fileCtr-1)

	#outLine = filename.strip('.csv') + ',' + str(fileCtr) + ',' + str(total_rain_precp) + ',' + str(total_rain_time) +',' + str(how_many_T) + '\n'
	#OutputList.append(outLine)
	fileCtr += 1
	
notRainDay = list()

for outlier in outlierData_3[1] :
	if outlier not in rainDayList :
		notRainDay.append(outlier)
		
print(notRainDay)

x = np.arange(0,302)
y = TravelList


plt.plot(x,y,'ro')
plt.plot(x,y)
'''
print(outlierData_1[0:2])
print(outlierData_2[0:2])
print(outlierData_3[0:2])
'''
#plt.plot([0,350],[outlierData_1[1],outlierData_1[1]],lw = 3)
#plt.plot([0,350],[outlierData_1[2] + std_range* outlierData_1[3],outlierData_1[2] + std_range* outlierData_1[3]],lw = 2)
plt.plot([0,350],[outlierData_1[2] - std_range* outlierData_1[3],outlierData_1[2] - std_range* outlierData_1[3]],lw = 2)
#plt.plot([0,350],[outlierData_2[2] + std_range* outlierData_2[3],outlierData_2[2] + std_range* outlierData_2[3]],lw = 2)
plt.plot([0,350],[outlierData_2[2] - std_range* outlierData_2[3],outlierData_2[2] - std_range* outlierData_2[3]],lw = 2)
#plt.plot([0,350],[outlierData_3[2] + std_range* outlierData_3[3],outlierData_3[2] + std_range* outlierData_3[3]],lw = 2)
plt.plot([0,350],[outlierData_3[2] - std_range* outlierData_3[3],outlierData_3[2] - std_range* outlierData_3[3]],lw = 2)

plt.xlabel("Day") 
plt.ylabel("Traveling") 
plt.title("Growing of YouBike System") 
	
plt.show()