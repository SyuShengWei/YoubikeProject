"""
open raw data
elimate the test station start in @
notice the code
"""
#code=utf-8
import codecs
import os

#open the file in code of utf-8
os.chdir("D:/project/Open data")
filename = raw_input("Enter file name:")
file = codecs.open(filename, 'r', 'utf-8')

#read data by line and store in list
data = file.readlines()
file.close()

#the funciotn of print data in order to now its type 
def printfile(data):
	i = 0
	for line in data:
		print line.encode('big5')
		i += 1
		if i > 5:break

#find the test station following by @ and store its posisiotn in temp list
temp = list()
count = 0
while count < len(data):
	if "@" in data[count]:
		temp.append(count)
	count += 1

temp.reverse()
printfile(data)
#elimate the data of test station
for count in temp:	
	del data[count]

newfolder = "elimatext"
if not os.path.exists(newfolder):
	os.makedirs(newfolder)
#change path in new fold
os.chdir("D:/project/Open data/elimatext")
#write new data in new file
out_file = open(filename, 'w')

for line in data:
	out_file.write(line.encode('big5'))
