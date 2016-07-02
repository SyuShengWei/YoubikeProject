import numpy as np
import matplotlib.pyplot as plt
import os
import codecs
from matplotlib.font_manager import FontProperties
statfile = codecs.open("D:/project/Open data/stations.txt", 'r', 'big5')
stations = statfile.readlines()
statfile.close()

font = FontProperties(fname=r"c:\windows\fonts\SimSun.ttc")

def readdata(filename):
	#read file 
	file = open(filename, 'r')
	data = file.readlines()
	file.close()
	temp = {}
	count = 0
	while count < len(data):
		temp[data[count].replace("\n", '')] = data[count + 1].replace("\n","")
		count += 2
	return temp

os.chdir("D:/project/Open data")
filename = input("Enter:")
data = readdata(filename)
for key in data:

	flow = data.get(key).split(" ")
	x = []
	y = []
	count = 0
	for item in flow:
		if item != "" and count%2 == 0:
			x.append(int(item))
		elif item !="" and count%2 == 1:
			y.append(float(item))
		count += 1
	fig = plt.figure(int(key))
	ax = fig.add_subplot(111)
	plt.title(stations[int(key) - 1], fontproperties = font)
	plt.xlim(0.5, 48.5)
	ax.set_xticks([2.5, 4.5, 6.5, 8.5, 10.5, 12.5, 14.5, 16.5, 18.5, 20.5, 22.5, 24.5, 
					26.5, 28.5, 30.5, 32.5, 34.5, 36.5, 38.5, 40.5, 42.5, 44.5, 46.5, 48.5])
	ax.set_xticklabels(["", 2, "", 4, "", 6, "", 8, "", 10, "", 12, "", 14, "", 16, "", 18, "", 20, "", 22, "", 24])
	plt.grid(True)
	
	plt.plot(x, y)
	plt.savefig("D://project/plot/in-step-averge/"+key.rjust(3,"0")+'.png')
