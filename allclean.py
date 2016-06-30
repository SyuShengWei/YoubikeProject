"""

"""
import os
import codecs

for filename in os.listdir("D:/project/Open data"):
	os.chdir("D:/project/Open data")
	if filename == "stations.txt":continue
	file = codecs.open(filename, 'r', 'utf8')
	data = file.readlines()
	file.close()
	
	#find the test station following by @ and store its posisiotn in temp list
	temp = list()
	count = 0
	while count < len(data):
		if "@" in data[count] or "2013-" in data[count] or "2014" not in data[count] or "2012" in data[count] or ",," in data[count]:
			temp.append(count)
		count += 1

	temp.reverse()
	print("Loading" + filename)
	#elimate the data of test station
	for count in temp:	
		del data[count]
		
	newfolder = "cleanData"
	if not os.path.exists(newfolder):
		os.makedirs(newfolder)

	os.chdir("D:/project/Open data/cleanData")
	newfile = open(filename, 'w')
	for line in data:
		newfile.write(",".join(line))

	newfile.close()
	break:
	