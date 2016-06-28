#code=utf-8

import os

statfile = open("D:/project/Open data/stations.txt", 'r')
stations = statfile.readlines()
statfile.close()

def readdata(filename):
	os.chdir("D:/project/Open data/elimatext/elimat2013/ceardata")
	file = open(filename, 'r')
	data = file.readlines()
	file.close()
	count = 0

	temp = list()

	for line in data:
		item = line.split(",")
		temp.append(item)
	return temp
for filename in os.listdir("D:/project/Open data/elimatext/elimat2013/ceardata"):
	print "Loading" + filename
	data = readdata(filename)

	splitbystep = [[]]*len(stations)

	count = 0
	for station in stations:
		temp = list()
		for line in data:
			if line[2]+"\n" == station:
				temp.append(line)
		splitbystep[count] = temp
		count += 1

	os.chdir("D:/project")
	newfolder = "split-by-rent"
	if not os.path.exists(newfolder):
		os.makedirs(newfolder)

	os.chdir("D:/project/split-by-rent")

	count = 0
	while count < len(stations):
		name = str(count+1)+".csv"
		if not os.path.exists(name):
			newfile = open(name, 'w')
		else: newfile = open(name, 'a')
		for lines in splitbystep[count]:
			for line in lines:
				newfile.write(line)
		count += 1
		newfile.close()
