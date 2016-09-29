'''
This code is use to Split every deta by Station
All data form is same as RegularForm
'''

import os 
import codecs
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
		new_dic = {stationInfo[0]:stationInfo[1]} # {number : stationName}
		StationDic.update(new_dic)
inFile.close()

#except
exceptList = list()
ctr = 0
for filename in os.listdir('C:/Users/SyuShengWei/Desktop/project/RegularForm'):
	if 'except' in filename : continue
	else :
		ctr +=1 
		print('File : ' + str(ctr) )
		#create a 164 elements list to store every station information
		DataList = list()
		for i in range(0,164,1):
			StationData = list()
			DataList.append(StationData)
		#open each file and read Data
		os.chdir('C:/Users/SyuShengWei/Desktop/project/RegularForm')
		inFile = open(filename,'r')
		titleLine = inFile.readline() #ignor the title
		while True :
			theLine = inFile.readline()
			if theLine == '' : break
			else:
				try :
					lineInfo = theLine.split(',')
					stationIndex = int(lineInfo[4])
					DataList[stationIndex].append(theLine)
				except:
					exceptList.append(theLine)
					print(theLine)
		inFile.close()
		#store the File

		os.chdir('C:/Users/SyuShengWei/Desktop/project')
		if not os.path.exists('RegularSplitByStation'):
			os.makedirs('RegularSplitByStation')
		
		for i in range(0,164,1):
			os.chdir('C:/Users/SyuShengWei/Desktop/project/RegularSplitByStation')
			stationName = StationDic[str(i)]
			if i <10:
				if not os.path.exists('00'+str(i)+'-'+stationName):
					os.makedirs('00'+str(i)+'-'+stationName)
				os.chdir('C:/Users/SyuShengWei/Desktop/project/RegularSplitByStation/'+'00'+str(i)+'-'+stationName)
			elif i <100:
				if not os.path.exists('0'+str(i)+'-'+stationName):
					os.makedirs('0'+str(i)+'-'+stationName)
				os.chdir('C:/Users/SyuShengWei/Desktop/project/RegularSplitByStation/'+'0'+str(i)+'-'+stationName)
			else :
				if not os.path.exists(str(i)+'-'+stationName):
					os.makedirs(str(i)+'-'+stationName)
				os.chdir('C:/Users/SyuShengWei/Desktop/project/RegularSplitByStation/'+str(i)+'-'+stationName)
			outFile = open(filename,'a+')
			outFile.write(titleLine)
			for element in DataList[i] :
				outFile.write(element)
			outFile.close()
