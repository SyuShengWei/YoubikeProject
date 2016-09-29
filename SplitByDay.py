import os
import codecs
import copy

whichFile = 1

exceptList = list()

for filename in  os.listdir('C:/Users/SyuShengWei/Desktop/project/cleanData'):
	if filename == 'checkList.csv' or filename == 'except.csv' :
		continue
	#dabug message
	print('File is :' + str(whichFile))
	#create 2D list to store data od each day
	MoonList = list()
	for i in range(0,31):
		DayList = list()
		MoonList.append(DayList)
	#read File
	os.chdir('C:/Users/SyuShengWei/Desktop/project/cleanData')
	inFile = open(filename,'r',)
	while True :
		theLine = inFile.readline()
		if theLine == '' :
			break
		else :
			lineInfo = theLine.split(',')
			if '2014-' in lineInfo[1] :
				rentDateInfo = lineInfo[1].split(' ')
				dayInfo = rentDateInfo[0].split('-')
				DayIndex = int(dayInfo[2]) - 1
				MoonList[DayIndex].append(theLine)
				#print(MoonList[DayIndex])
				
			elif '2014/' in lineInfo[1] :
				rentDateInfo = lineInfo[1].split(' ')
				dayInfo = rentDateInfo[0].split('/')
				DayIndex = int(dayInfo[2]) - 1
				MoonList[DayIndex].append(theLine)
			else :
				exceptList.append(theLine)
	#output files
	os.chdir('C:/Users/SyuShengWei/Desktop/project')
	if not os.path.exists('SplitByDay(2014-OO-XX)') :
		os.makedirs('SplitByDay(2014-OO-XX)')
		
	os.chdir('C:/Users/SyuShengWei/Desktop/project/SplitByDay(2014-OO-XX)')
	
	if whichFile != 10 :
		Moon = '0' + str(whichFile)
	else :
		Moon = str(whichFile)
		
	dayCtr = 1
	
	for elementList in MoonList :
		if len(elementList) != 0 :
			if dayCtr < 10 :
				Day = '0' + str(dayCtr) 
			else :
				Day = str(dayCtr)
			outFile = open('2014-' + Moon + '-' + Day + '.csv','a+')
			for element in elementList :
				element = element.strip('\n')
				outFile.write(element)
				outFile.write('\n')
			outFile.close()
			dayCtr+=1
		else :
			print('Have no day : '+str(MoonList.index(elementList) + 1))
	whichFile += 1

print('output except')
os.chdir('C:/Users/SyuShengWei/Desktop/project/splitByDay')
outFile = open('except.csv','a+')
for element in exceptList :
	outFile.write(element)
	outFile.wirte('\n')