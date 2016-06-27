#code=utf-8
import os
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
		
	for line in temp:
		print line[2]
		count += 1
		if count > 5:break
	return temp