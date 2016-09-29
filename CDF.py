#this file is used to define the CDF class

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