'''
This code is used to define a function which can find the outlier in a list
Input : 1. list which store the data
		2. how many STD will use to find outlier
		3. resulf data which after one or more times to find outlier and delete the outlier
		(3 is used when you want to check many times)
Output: 1.index which element biger then uper  bound
		2.index which element biger then lower bound
		3.Average  of original data
		4.STD of original data
'''
import os
import numpy as np
import matplotlib.pyplot as plt

def outlier(List_data,STDrange = 3,List_afterData = []):
	
	if len(List_afterData) != 0 : 
		Array_data = np.asarray(List_afterData)
	else :
		Array_data = np.asarray(List_data)
	Data_average = np.mean(Array_data)
	#print(Data_average)
	Data_STD	 = np.std(Array_data )
	#print(Data_STD)
	
	List_Over_outlierValue = list()
	List_Below_outlierValue = list()
	
	List_Over_outlierIndex = list()
	List_Below_outlierIndex = list()
	
	for element in List_data :
		if element == None : 
			continue
		elif element > Data_average + STDrange* Data_STD  :
			if element not in List_Over_outlierValue :
				List_Over_outlierValue.append(element)
		elif  element <  Data_average - STDrange* Data_STD :
			if element not in List_Below_outlierValue :
				List_Below_outlierValue.append(element)
				
				
				
	for outlierValue in List_Over_outlierValue :
		indexCTR = 0
		for element in List_data :
			if outlierValue == element :
				List_Over_outlierIndex.append(indexCTR)
			indexCTR += 1
			
	for outlierValue in List_Below_outlierValue :
		indexCTR = 0
		for element in List_data :
			if outlierValue == element :
				List_Below_outlierIndex.append(indexCTR)
			indexCTR += 1
	
	
	returnList = [List_Over_outlierIndex,List_Below_outlierIndex,Data_average,Data_STD]
	
	return returnList




