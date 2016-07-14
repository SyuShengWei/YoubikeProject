"""
compute every station's average flow num according weekday 
"""
from datetime import datetime, date
import os
import codecs
statfile = codecs.open("D:/project/Open data/stations.txt", 'r', 'big5')
stations = statfile.readlines()
statfile.close()

os.chdir("D:/project/flow-day-by-sta/")
def readdata(filename):
	#read file 
	os.chdir("D:/project/flow-day-by-sta/")
	file = open(filename, 'r')
	data = file.readlines()
	file.close()
	temp = {}
	count = 0
	while count < len(data):
		temp[data[count].replace("\n", '')] = data[count + 1].replace("\n","")
		count += 2
	return temp
for filename in os.listdir("D://project/flow-day-by-sta/"):
	data = readdata(filename)
	y = [[0 for col in range(48)] for row in range(7)]
	days = [0]*7
	x = []
	for key in data:
		flow = data.get(key).split(" ")
		count = 0
		time = key.split("-")
		timer = date(int(time[0]), int(time[1]), int(time[2]))
		days[timer.weekday()] += 1
		for item in flow:
			if item != "" and count%2 == 0:
				x.append(int(item))
			elif item !="" and count%2 == 1:
				y[timer.weekday()][int((count - 1)/2)] += float(item)
			count += 1

	os.chdir("D:/project/Open data")
	if not os.path.exists("flow-weekday.txt"):
		newfile = open("flow-weekday.txt", 'w')
	else: newfile = open("flow-weekday.txt", 'a')
	newfile.write(filename.rstrip(".txt") + "\n")
	
	ind = 0
	while ind < len(days):
		period = 0
		newfile.write(str(ind+1) +"\n")
		for num in y[ind]:	
			temp = round(num/days[ind], 4)
			newfile.write(str(x[period]) + " ")
			newfile.write(str(temp) + " ")
			period += 1
		newfile.write("\n")
		ind += 1