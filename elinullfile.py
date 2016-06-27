#code=utf-8
import os

		
for filename in os.listdir("D:/project/Open data/elimatext/elimat2013"):
	os.chdir("D:/project/Open data/elimatext/elimat2013")
	if filename == "ceardata":continue
	file = open(filename, 'r')
	data = file.readlines()
	file.close()
	print "Loading %s" %filename
	count = 0
	temp = list()

	while count < len(data):
		if "2014" not in data[count] or "2012" in data[count] or ",," in data[count]:
				temp.append(count)
		count += 1

	print len(temp)

	temp.reverse()
	for count in temp:
		del data[count]

	newfolder = "ceardata"
	if not os.path.exists(newfolder):
		os.makedirs(newfolder)

	os.chdir("D:/project/Open data/elimatext/elimat2013/ceardata")
	newfile = open(filename, 'w')
	for line in data:
		newfile.write(line)

	newfile.close()


