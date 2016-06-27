"""
elimate the data in the time of 2013
"""
#code=utf-8
import os

#change path and open the file of the name which is entered by user
os.chdir("D:/project/Open data/elimatext")
filename = raw_input("Enter file name:")
file = open(filename, 'r')

#read in line in the list
data = file.readlines()
file.close()
#build new list to store the position of the data include 2013
count = 0
temp = list()
while count < len(data):
	if "2013-" in data[count]:
		temp.append(count)
	count += 1

#print the length of data and data include 2013
print len(temp)
print len(data)

#elimate the data inculud 2013
temp.reverse()
for count in temp:
	del data[count]

#check again
print len(data)
temp2 = list()
count = 0
while count < len(data):
	if "2013-" in data[count]:
		temp2.append(count)
	count += 1

print len(temp2)

#build new fold in the fold is not exist
newfolder = "elimat2013"
if not os.path.exists(newfolder):
	os.makedirs(newfolder)
#change path in new fold
os.chdir("D:/project/Open data/elimatext/elimat2013")
#write new data in new file
newfile = open(filename, 'w')
for line in data:
	newfile.write(line)


