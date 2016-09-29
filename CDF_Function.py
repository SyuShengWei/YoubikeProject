import os

class CDF :
	#member data
	dataList = list()
	len_of_list = len(list())
	probability_of_each_test = 0
	#initialization function
	
	
	def __init__(self,dataList):
		self.dataList = dataList
		self.len_of_list = len(dataList)
	#call:CDF.prob_within_X(x,precise) x is the input value ,precise is the round of digit
	def prob_within_X(self,X_value,precise = 2):
		self.testList = list()
		self.testList = self.dataList 
		self.testList.append(X_value)
		self.testList.sort()
		self.len_of_test = len(self.testList)
		self.probability_of_each_test = round(1/self.len_of_test,precise)
		self.probList = list()
		for i in range(0,self.len_of_test,1):
			self.probList.append((i+1) * self.probability_of_each_test)
		for i in range(self.len_of_test - 1,-1,-1):
			if self.testList[i] == X_value:
				self.probIndex = i
				break
		if self.probList[self.probIndex] > 1 :
			self.probList[self.probIndex] = 1
		return self.probList[self.probIndex]
	
def CDF_Function(O_station,D_station,X_value,if_rain = 0,if_holiday = 0,precise = 10):
	if if_rain == 0 and if_holiday == 0:
		dataKind = 0
	elif if_rain == 1 and if_holiday == 0:
		dataKind = 1
	elif if_rain == 0 and if_holiday == 1:
		dataKind = 2
	elif if_rain == 1 and if_holiday == 1:
		dataKind = 3
	else:
		print('wrong input , please try again')
		return 
	if O_station not in range(0,164) or D_station not in range(0,164):
		print('wrong input , please try again')
		return
	theCDF = CDF(TravelingTimeDataMatrix[O_station][D_station][dataKind])
	the_probability = theCDF.prob_within_X(X_value,precise)
	return the_probability

TravelingTimeDataMatrix = list()
for i in range (0,164):
	distinationList = list()
	for j in range(0,164):
		eachKindDataList = list()
		for k in range(0,4):
			dataList = list()
			eachKindDataList.append(dataList)
		distinationList.append(eachKindDataList)
	TravelingTimeDataMatrix.append(distinationList)
#input data
print('Reading InFile')
os.chdir('C:/Users/SyuShengWei/Desktop/project') #you can change you path here
inFile = open('CDF_Data.txt','r')
theData = inFile.readlines()
for i in range(0,len(theData)):
	OIndex = int(i / 164)
	DIndex = i % 164
	theData[i] = theData[i].strip('\n')
	anODData = theData[i].split('+')
	for k in range(0,4):
		aKindData = anODData[k].split(',')
		for element in aKindData:
			if element != '-1':
				TravelingTimeDataMatrix[OIndex][DIndex][k].append(int(element))
			else :
				continue