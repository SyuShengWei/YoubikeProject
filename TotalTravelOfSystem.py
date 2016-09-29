import os 
import numpy as np
import matplotlib.pyplot as plt

TravelList  = list()
DateList 	= list()
CTRList		= list()
OutFileList = list() 

fileCTR = 0

for filename in os.listdir('C:/Users/SyuShengWei/Desktop/project/RegularForm'):
	if 'except' in filename : continue
	else :
		#debug message
		fileCTR += 1 
		print('File : ' + str(fileCTR))
	
	
		os.chdir('C:/Users/SyuShengWei/Desktop/project/RegularForm')
		inFile = open(filename,'r')
		titleLine  = inFile.readline()
		travelCTR = 0
	
		checkline = inFile.readline()
		lineInfo = checkline.split(',')
		WeekDay = lineInfo[6]
		travelCTR +=1
		
		while True:
			theLine = inFile.readline()
			if theLine == '' : break
			else : travelCTR += 1 
	
		TravelList.append(travelCTR)
		DateList.append(filename.strip('.csv'))
		CTRList.append(fileCTR)
	
		outLine = filename.strip('.csv') + ',' + str(fileCTR) +',' +str(travelCTR) + ',' + WeekDay + '\n'
		OutFileList.append(outLine)

os.chdir('C:/Users/SyuShengWei/Desktop/project/')
outFile = open('TotalTravelOfSystem.txt','a+')
outFile.write('This file is used to record the total travel of each day \n')
for element in OutFileList:
	outFile.write(element)
outFile.close()

'''
x = np.array(CTRList)
y = np.array(TravelList)

plt.plot(x,y,'ro')
plt.plot(x,y)

plt.xlabel("Day") 
plt.ylabel("Traveling") 
plt.title("Growing of YouBike System") 

plt.show()
'''