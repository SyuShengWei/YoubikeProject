#code=utf-8
import os

os.chdir("D:/project/Open data/elimatext/elimat2013/ceardata")
stastions = list()

def readdata(filename):
	os.chdir("D:/project/Open data/elimatext/elimat2013/ceardata")
	#filename = "20140201-28DIGES.csv"
	file = open(filename, 'r')
	data = file.readlines()
	file.close()
	count = 0
	print "Loading %s" %filename
	temp = list()

	for line in data:
		item = line.split(",")
		temp.append(item)
		
#	for line in temp:
#		print line[2]
#		count += 1
#		if count > 5:break
		
	return temp


stastions = list()
for filename in os.listdir("D:/project/Open data/elimatext/elimat2013/ceardata"):
	data = readdata(filename)
	for line in data:
		if line[2] not in stastions:
			stastions.append(line[2])
			print line[2]

print len(stastions)
for stastion in stastions:	
	print stastion

os.chdir("D:/project/Open data")
#write new data in new file
out_file = open("stations.txt", 'w')

for line in stastions:
	out_file.write(line)
	out_file.write("\n")
	