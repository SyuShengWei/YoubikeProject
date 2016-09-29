import os
import codecs
import copy

exceptList = list()
whichFile = 1
for filename in  os.listdir('C:/Users/SyuShengWei/Desktop/project/Open data'):
	tempList = list()
	print('File : '+str(whichFile))
	os.chdir('C:/Users/SyuShengWei/Desktop/project/Open data')
	inFile = codecs.open(filename, 'r', 'utf8')
	while True:
		theLine = inFile.readline()
		if theLine =='':
			break
		else :
			if '@' in theLine or '2013' in theLine or '2014' not in theLine or "2012" in theLine or ",," in theLine:
				continue
			else :
				lineInfo = theLine.split(',')
				theLine = theLine.strip('\n')
				theLine = theLine.strip('\r')
				if '2014-0'+str(whichFile) in lineInfo[1] and whichFile <= 9:
					tempList.append(theLine)
				elif '2014-10' in lineInfo[1] and whichFile == 10 :
					tempList.append(theLine)
				else :
					exceptList.append(theLine)
	inFile.close()
	os.chdir('C:/Users/SyuShengWei/Desktop/project')
	newFolder = "cleanData"
	if not os.path.exists(newFolder):
		os.makedirs(newFolder)
	os.chdir('C:/Users/SyuShengWei/Desktop/project/cleanData')
	outFile = open(filename,'a+')
	for i in range(0,len(tempList)):
		outFile.write(tempList[i])
		outFile.write('\n')
	outFile.close()
	whichFile += 1;
os.chdir('C:/Users/SyuShengWei/Desktop/project/cleanData')
print(len(exceptList))

print('start to check')

chechList = copy.copy(exceptList)
ctr = 0

for element in exceptList:
	theLine = element
	lineInfo = theLine.split(',')
	#print(lineInfo[1])
	if '2014-01' in lineInfo[1] or '2014/1' in lineInfo[1]:
		outFile = open('20140101-31DIGES.csv','a+')
		outFile.write(theLine)
		outFile.write('\n')
		outFile.close()
		chechList.remove(element)
		ctr +=1
	elif '2014-02' in lineInfo[1] or '2014/2' in lineInfo[1]:
		outFile = open('20140201-28DIGES.csv','a+')
		outFile.write(theLine)
		outFile.write('\n')
		outFile.close()
		chechList.remove(element)
		ctr +=1
	elif '2014-03' in lineInfo[1] or '2014/3' in lineInfo[1]:
		outFile = open('20140301-0331DIGES.csv','a+')
		outFile.write(theLine)
		outFile.write('\n')
		outFile.close()
		chechList.remove(element)
		ctr +=1
	elif '2014-04' in lineInfo[1] or '2014/4' in lineInfo[1]:
		outFile = open('20140401-30DIGES.csv','a+')
		outFile.write(theLine)
		outFile.write('\n')
		outFile.close()
		chechList.remove(element)
		ctr +=1
	elif '2014-05' in lineInfo[1] or '2014/5' in lineInfo[1]:
		outFile = open('20140501-31DIGES.csv','a+')
		outFile.write(theLine)
		outFile.write('\n')
		outFile.close()
		chechList.remove(element)
		ctr +=1
	elif '2014-06' in lineInfo[1] or '2014/6' in lineInfo[1]:
		outFile = open('20140601-30DIGES.csv','a+')
		outFile.write(theLine)
		outFile.write('\n')
		outFile.close()
		chechList.remove(element)
		ctr +=1
	elif '2014-07' in lineInfo[1] or '2014/7' in lineInfo[1]:
		outFile = open('20140701~0731DIGES.csv','a+')
		outFile.write(theLine)
		outFile.write('\n')
		outFile.close()
		chechList.remove(element)
		ctr +=1
	elif '2014-08' in lineInfo[1] or '2014/8' in lineInfo[1]:
		outFile = open('20140801~0831DIGES.csv','a+')
		outFile.write(theLine)
		outFile.write('\n')
		outFile.close()
		chechList.remove(element)
		ctr +=1
	elif '2014-09' in lineInfo[1] or '2014/9' in lineInfo[1]:
		outFile = open('20140901~0930DIGES.csv','a+')
		outFile.write(theLine)
		outFile.write('\n')
		outFile.close()
		chechList.remove(element)
		ctr +=1
	elif '2014-10' in lineInfo[1] or '2014/10' in lineInfo[1]:
		outFile = open('20141001~1031DIGES.csv','a+')
		outFile.write(theLine)
		outFile.write('\n')
		outFile.close()
		chechList.remove(element)
		ctr +=1
	else :
		print(element)
		
outFile = open('except.csv','a+')
for element in exceptList:
	outFile.write(element)
	outFile.write('\n')
outFile.close()

outFile = open('checkList.csv','a+')
outFile.write('Have check : ' + str(ctr))
for element in checkList:
	outFile.write(element)
	outFile.write('\n')
outFile.close()