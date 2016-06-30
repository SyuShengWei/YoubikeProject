#依照借車站拆檔
import csv
file = open("/Users/HuangYungHan/Desktop/stationss.txt", 'r', encoding = 'UTF-8') #	打開存放station的文件
stations = list() #用來存放所有的站名
for row in file.readlines(): #將station一一存進list(stations)
	row = row.strip('\n') #去掉換行字元
	stations.append(row) 
file.close()

#根據借出站將檔案拆開
for filename in stations: 
	f = open('/Users/HuangYungHan/Desktop/20140101-31DIGES.csv', 'r') #打開單月資料
	fw = open("/Users/HuangYungHan/Desktop/ubike/"+filename+".csv","w")  #開一個新的csv檔(以origin命名)
	w = csv.writer(fw)   
	temp = list()
	for row in csv.reader(f):  
		temp = row
		if filename in temp[2]:
			w.writerow(row) 
	fw.close() 
	f.close()




