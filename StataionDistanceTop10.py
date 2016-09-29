import os 

class Station :
	
	def __init__(self,station_num,lat,long):
		self.station_num = station_num
		self.lat		 = lat
		self.long 		 = long
		self.Near_Station 	  = list()
		self.Near_Staiton_Dis = list()
		for i in range(0,10):
			self.Near_Station.append(-1)
			self.Near_Staiton_Dis.append(9999999999)
			
Station_List = list()
	
	
os.chdir('C:/Users/SyuShengWei/Desktop/project/stationInfomation')
inFile = open('StationInfomation.txt','r')
titleLine = inFile.readline()
Data_List = inFile.readlines()
for index in range(0,164):
	The_Line = Data_List[index].strip('\n')
	Line_Info = The_Line.split(',')
	station_num = int(Line_Info[0])
	location_lat  = float(Line_Info[2])
	locarion_long = float(Line_Info[3])
	station = Station(station_num,location_lat,locarion_long)
	Station_List.append(station)
inFile.close()	
	
for index in range(0,164):
	the_Station = Station_List[index]
	for comp_index in range(0,164):
		if index == comp_index : continue
		else:
			comp_Station = Station_List[comp_index]
			station_dis  = abs(the_Station.lat - comp_Station.lat) + abs(the_Station.long - comp_Station.long)
			for i in range(0,10):
				if station_dis < the_Station.Near_Staiton_Dis[i]:
					the_Station.Near_Staiton_Dis.insert(i,station_dis)
					the_Station.Near_Station.insert(i,comp_Station.station_num)
					del(the_Station.Near_Staiton_Dis[10])
					del(the_Station.Near_Station[10])
					break
				else : continue
	
outFile = open('NearStation_10_NEW.txt','a')
for station in Station_List:
	for i in range(0,10):
		outFile.write(str(station.Near_Station[i]))
		if i != 9 :
			outFile.write(',')
		else:
			outFile.write('\n')
	