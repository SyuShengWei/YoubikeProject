"""
split per station by 30 min a intern
"""
import os
#loading name of station
statfile = open("D:/project/Open data/stations.txt", 'r')
stations = statfile.readlines()
statfile.close()

#read file in split by O/D,and return data, and type like 2014-01-01 14:17:18

def readdata(filename):
	#read file 
	os.chdir("D:/project/split-by-Ori")
	file = open(filename, 'r')
	data = file.readlines()
	file.close()
	#store data splited by ",", and ignore change line
	temp = list()
	timein = list()
	for line in data:
		if line == "\n": continue
		item = line.split(",")
		temp.append(item)
	#just need time of O/D
	for data in temp:
		timein.append(data[1])
	return timein

#check it time and count average number of rent or borrow in every 30 mininte
for filename in os.listdir("D://project/split-by-Ori"):
	data = readdata(filename)
	#buide list which length is 48, every 30 miniute can sperate a day in 48 part
	flow_in =[0]*48
	#the flow_in list is [00:00~00:29, 00:30~10:29.......]
	
	#check which part it belong
	for time in data:
		pos = time.find(" ")#find " ", it can sure position, before is day and behind is time
		hr = int(time[pos+1:pos+3])#check hour amd store in int
		min = 0
		if int(time[pos+4:pos+6]) < 30:#check minutes amd store in int
			min = 0
		else: min = 1
		
		flow_in[hr*2 + min] += 1#find the part its belong
	count = 0
	#divide days, in this assume it all run ten months equal to 304 days
	while count <len(flow_in):
		temp = round(flow_in[count]/ 304, 4)
		flow_in[count] = temp
		count += 1
	print(stations[int(filename.rstrip(".csv"))-1])
	#print(flow_in)
	
	#store all data in txt 
	os.chdir("D:/project/Open data")
	#check the file is exist ot not, if there has file and use 'a' add in the finally
	#if there are not having a file and use 'w' and create one
	if not os.path.exists("out_flow.txt"):
			newfile = open("out_flow.txt", 'w')
	else: newfile = open("out_flow.txt", 'a')
	
	#store a station number in the first and change line
	name = filename.rstrip(".csv")
	newfile.write(name + "\n")
	#store data un the need formats
	#the formate is "period1 average number in period1 peroid2....."
	count_index = 1
	for line in flow_in:
		newfile.write(str(count_index)+" ")
		count_index += 1
		newfile.write(str(line)+" ")
	newfile.write("\n")

	newfile.close()
	