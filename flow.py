#計算各站的借車數量與還車數量 
import csv
file = open("/Users/HuangYungHan/Desktop/stationss.txt", 'r', encoding = 'UTF-8') #	打開存放station的文件
stations = list() #用來存放所有的站名
for row in file.readlines(): #將station一一存進list(stations)
	row = row.strip('\n') #去掉換行字元
	stations.append(row) 
file.close()


fw = open("/Users/HuangYungHan/Desktop/rentQ.csv","w") 
w = csv.writer(fw)
date = ["station/date","01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24","25","26","27","28","29","30","31"]
w.writerow(date) 
temp = list()
c=0

for filename in stations: 
	rent = list()
	rent.append(filename+ ' out')
	for i in range(1,32,1):
		f = open('/Users/HuangYungHan/Desktop/ubike/'+filename+'.csv', 'r', encoding = 'UTF-8')
		for row in csv.reader(f):  
			temp = row
			if "2014-01-" + date[i] in temp[1]:
				c = c+1
		f.close()
		rent.append(c)
		c = 0
	w.writerow(rent) 
	rent.clear()
	rent.append(filename+' in')
	for i in range(1,32,1):
		f = open('/Users/HuangYungHan/Desktop/ubikeD/'+filename+'.csv', 'r', encoding = 'UTF-8')
		for row in csv.reader(f):  
			temp = row
			if "2014-01-" + date[i] in temp[1]:
				c = c+1
		f.close()
		rent.append(c)
		c = 0
	w.writerow(rent) 






