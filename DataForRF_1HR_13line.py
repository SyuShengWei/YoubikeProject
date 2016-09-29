'''
1.日期 2.時段 3.星期幾 4.是假日嗎 5.天氣 6.雨量 7.氣溫 8.紫外線 9.前期還車數 (10.附近站點前期還車數、借車數)
Output：
1.借車數 2.還車數 3.流向top10的車站的歸還比例(OD rate)



step1:計算OD -> [302*24(時段)][O][Data->借車,還車]

step2.依時段給予日期資訊

'''

import os 
import math
import calendar

#需要資料輸入
#1.日期、星期
Day_List = list() #[2014-**-**,星期]

os.chdir('C:/Users/SyuShengWei/Desktop/project/')
inFile = open('TotalTravelOfSystem.txt','r')
titleLine = inFile.readline()
Data_List = inFile.readlines()
for i in range(0,len(Data_List)):
	theLine  = Data_List[i].strip('\n')
	lineInfo = theLine.split(',')
	infoList = [lineInfo[0],lineInfo[3]]
	Day_List.append(infoList)
inFile.close()
#2.星期轉換
Week_Day_Dic = {}
mon_dic 	= {'1':'Mon'}
tues_dic 	= {'2':'Tues'}
wednes_dic 	= {'3':'Wednes'}
thurs_dic 	= {'4':'Thurs'}
fri_dic 	= {'5':'Fri'}
satur_dic 	= {'6':'Satur'}
sun_dic 	= {'7':'Sun'}
Week_Day_Dic.update(mon_dic)
Week_Day_Dic.update(tues_dic)
Week_Day_Dic.update(wednes_dic)
Week_Day_Dic.update(thurs_dic)
Week_Day_Dic.update(fri_dic)
Week_Day_Dic.update(satur_dic)
Week_Day_Dic.update(sun_dic)
#3.假日
Holiday_List = list()
inFile = open('C:/Users/SyuShengWei/Desktop/project/holiday.txt','r')
while True :
	theLine = inFile.readline()
	if theLine =='' : break
	else : 
		Holiday_List.append(theLine.strip('\n'))
inFile.close()
#4.Top 10 Near
Near_Station_List = list()

inFile = open('C:/Users/SyuShengWei/Desktop/project/stationInfomation/NearStation_latlong10.txt','r')
Data_List = inFile.readlines()
for theLine in Data_List :
	theLine = theLine.strip('\n')
	lineInfo = theLine.split(',')
	Near_Station = list()
	for info in lineInfo :
		Near_Station.append(int(info))
	Near_Station_List.append(Near_Station)
#5.天氣
Weather_List = list()

for filename in os.listdir('C:/Users/SyuShengWei/Desktop/project/WeatherDataWithTemperature'):
	os.chdir('C:/Users/SyuShengWei/Desktop/project/WeatherDataWithTemperature')
	inFile = open(filename,'r')
	titleLine = inFile.readline()
	Data_List = inFile.readlines()
	for theLine in Data_List:
		infoLine = theLine.strip('\n')
		Weather_List.append(infoLine)
	inFile.close()

#6.OD TOP 10 Station
Top_OD_List = list()
inFile = open('C:/Users/SyuShengWei/Desktop/project/ODR_Top10.txt','r')
Data_List = inFile.readlines()
for dataLine in Data_List:
	theLine = dataLine.strip('\n')
	Line_Info = theLine.split(',')
	Info_List = list()
	for data in Line_Info:
		Info_List.append(int(data))
	Top_OD_List.append(Info_List)
#
#Step 1 Record Rent OD and return OD
TravelRecord = list() #[302*24(時段)][Stataion][Data->借車,還車]
for peroid in range(0,(302*24)):
	Peroid_Data_List = list()
	for Station in range(0,164):
		Data_List = [0,0]
		Peroid_Data_List.append(Data_List)
	TravelRecord.append(Peroid_Data_List)
day_ctr = 0	

ODR_Record_1HR = list()
for O in range(0,164):
	O_List = list()
	for D in range(0,164):
		D_List = list()
		for peroid in range(0,(24*302)):
			peroid_record = 0
			D_List.append(peroid_record)
		O_List.append(D_List)
	ODR_Record_1HR.append(O_List)

Total_ODRecord_1HR = list()	
for O in range(0,164):
	O_List = list()
	for peroid in range(0,(24*302)):
		peroid_record = 0
		O_List.append(peroid_record)
	Total_ODRecord_1HR.append(O_List)


for filename in os.listdir('C:/Users/SyuShengWei/Desktop/project/RegularForm'):
	
	os.chdir('C:/Users/SyuShengWei/Desktop/project/RegularForm')
	inFile = open(filename,'r')
	titleLine = inFile.readline()
	Data_List = inFile.readlines()
	for theLine in Data_List:
		theLine = theLine.strip('\n')
		lineInfo = theLine.split(',')
		O_index = int(lineInfo[4])
		D_index = int(lineInfo[5])
		rent_peroid = int(int(lineInfo[1])/(60*60))
		rent_peroid_index = (day_ctr * 24) + rent_peroid 	# 1天24時段
		return_peroid = int(int(lineInfo[3])/(60*60))			
		return_peroid_index = (day_ctr * 24) + return_peroid
		TravelRecord[rent_peroid_index][O_index][0] += 1
		TravelRecord[return_peroid_index][D_index][1] += 1
		ODR_Record_1HR[O_index][D_index][rent_peroid_index] += 1
		Total_ODRecord_1HR[O_index][rent_peroid_index] += 1
	day_ctr += 1

	

os.chdir('C:/Users/SyuShengWei/Desktop/project')
if not os.path.exists('DataForFR_1HR_13Line'):
	os.makedirs('DataForFR_1HR_13Line')
os.chdir('C:/Users/SyuShengWei/Desktop/project/DataForFR_1HR_13Line')

#1.日期 2.時段 3.星期幾 4.是假日嗎 5.天氣 6.雨量 7.氣溫 8.紫外線 9.前期還車數 (10.附近站點前期還車數、借車數)

for station in range(0,164):
	outFile = open(str(station).rjust(3,'0') + '.csv','a')
	outFile.write('Date,Peroid,Weekday,if_holiday,if_rain,Precp,Tempture,UV,Last_Peroid_Retrun,')
	#outFile.write('NearStataion1_Rent,NearStataion1_Return,NearStataion2_Rent,NearStataion2_Return,NearStataion3_Rent,NearStataion3_Return,NearStataion4_Rent,NearStataion4_Return,NearStataion5_Rent,NearStataion5_Return,')
	#outFile.write('NearStataion6_Rent,NearStataion6_Return,NearStataion7_Rent,NearStataion7_Return,NearStataion8_Rent,NearStataion8_Return,NearStataion9_Rent,NearStataion9_Return,NearStataion10_Rent,NearStataion10_Return,')
	for i in range(0,10):
		outFile.write(str(Near_Station_List[station][i]) + 'Rent,' + str(Near_Station_List[station][i]) + 'Return,' )
	outFile.write('Rent_Num,Return_Num,')
	for i in range(0,10):
		outFile.write(str(Top_OD_List[station][i]) + ',')
	outFile.write('other_ODR \n')
	for peroid in range(0,(302*24)):
		day_index = int(peroid/24)
		#1.日期
		date = Day_List[day_index][0]
		#2.時段
		peroid_index = peroid%24
		#3.星期
		week_day = Week_Day_Dic[Day_List[day_index][1]]
		#4.假日?
		if date in Holiday_List :
			if_holiday = 'Y'
		else :
			if_holiday = 'N'
		#5.天氣
		Weather_Info = Weather_List[peroid].split(',')	
		if Weather_Info[2] != '0.0':
			if_rain = 'Y'
		else :
			if_rain = 'N'
		#6.雨量
		precp = Weather_Info[2]
		#7.氣溫 
		tempture = Weather_Info[4]
		#8.紫外線
		uvb = Weather_Info[5]
		#9.前期還車數
		if peroid == 0 :
			last_peroid_return = 0
		else :
			last_peroid_return = TravelRecord[peroid-1][station][1]
		#10.附近10站前期借車還車
		Last_Peroid_Near_Stataion_Rent = list()
		Last_Peroid_Near_Stataion_Return = list()
		for i in range(0,10):
			if peroid ==0 :
				Last_Peroid_Near_Stataion_Rent.append(0)
				Last_Peroid_Near_Stataion_Return.append(0)
			else:
				near_station_index = int(Near_Station_List[station][i])
				Last_Peroid_Near_Stataion_Rent.append(TravelRecord[peroid-1][near_station_index][0])
				Last_Peroid_Near_Stataion_Return.append(TravelRecord[peroid-1][near_station_index][1])
		#1.借車數 2.還車數 3.流向top10的車站的歸還比例(OD rate)
		rent_num = TravelRecord[peroid][station][0]
		return_num = TravelRecord[peroid][station][1]
		#set output line 
		output_line = date + ',' + str(peroid_index+1) + ',' + week_day + ',' + if_holiday + ',' + if_rain + ',' + precp + ',' + tempture + ',' +  uvb + ',' + str(last_peroid_return) + ','
		for i in range(0,10):
			output_line += str(Last_Peroid_Near_Stataion_Rent[i]) + ',' + str(Last_Peroid_Near_Stataion_Return[i]) + ','
		output_line += str(rent_num) + ',' + str(return_num) + ','
		
		left_ODR = 1.0
		for i in range(0,10):
			if  Total_ODRecord_1HR[station][peroid] == 0 :
				ODR = 0
			else:	
				ODR = round(ODR_Record_1HR[station][Top_OD_List[station][i]][peroid] / Total_ODRecord_1HR[station][peroid],5)
			output_line += str(ODR).ljust(6,'0') + ','
			left_ODR -= ODR
		output_line += str(left_ODR).ljust(6,'0') + '\n'
		
		outFile.write(output_line)
	outFile.close()
	