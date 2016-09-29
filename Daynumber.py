import os

dayNum = 0
outList = list()
for filename in os.listdir('C:/Users/SyuShengWei/Desktop/project/RegularForm'):
	dayNum += 1
	outLine = filename.strip('.csv') + ',' + str(dayNum) + '\n'
	outList.append(outLine)
	
os.chdir('C:/Users/SyuShengWei/Desktop/project')
outFile = open('DayNumber.txt','a+') 
for element in outList :
	outFile.write(element)
outFile.close()