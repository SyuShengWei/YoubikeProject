which_moon = '00' 
which_infile = 'fileNameWithoutCSV'
inFile = open('c:/Users/SyuShengWei/Desktop/Youbike/Open data/'+which_infile+'.csv','r',encoding ='UTF-8')

for x in range(1,10,1):
	outFile = open ('c:/Users/SyuShengWei/Desktop/Youbike/by_date/'+ which_moon +'/2014-' + which_moon + '-0' + str(x) +'.csv','a+')
	outFile.write('扣款時間           ,借車時間,借車場站,還車時間,還車場站,租用(分) \n')
	outFile.close()
for x in range(10,32,1):
	outFile = open ('c:/Users/SyuShengWei/Desktop/Youbike/by_date/' + which_moon + '/2014-' + which_moon + '-' + str(x) +'.csv','a+')
	outFile.write('扣款時間           ,借車時間,借車場站,還車時間,還車場站,租用(分) \n')
	outFile.close()
	
outFile = open ('c:/Users/SyuShengWei/Desktop/Youbike/by_date/' + which_moon + '/uselessDeta.csv','a+')
outFile.write('扣款時間           ,借車時間,借車場站,還車時間,還車場站,租用(分) \n')
outFile.close()

ctr = 0
while True :	
	theLine = inFile.readline()
	ctr = ctr+1
	#print(theLine)
	if theLine == '' : break
	else :
		judgement = list()
		judgement = theLine.split(",")
		if '2014-' + which_moon + '-' not in judgement[1]:
			outFile = open ('c:/Users/SyuShengWei/Desktop/Youbike/by_date/' + which_moon + '/uselessDeta.csv','a+')
			outFile.write(theLine)
			
			ctr=ctr+1
			print(ctr)
		else:
				whichFile = str(judgement[1]).split(' ')
				outFile = open ('c:/Users/SyuShengWei/Desktop/Youbike/by_date/' + which_moon + '/'+ whichFile[0] +'.csv','a+')
				outFile.write(theLine)
				
				ctr=ctr+1
				print(ctr)
				#print(whichFile[0])


for x in range(1,10,1):
	outFile = open ('c:/Users/SyuShengWei/Desktop/Youbike/by_date/' + which_moon + '/2014-' + which_moon + '-0' + str(x) +'.csv','a+')
	outFile.close()
for x in range(10,32,1):
	outFile = open ('c:/Users/SyuShengWei/Desktop/Youbike/by_date/' + which_moon + '/2014-' + which_moon + '-' + str(x) +'.csv','a+')
	outFile.close()
	
outFile = open ('c:/Users/SyuShengWei/Desktop/Youbike/by_date/' + which_moon + '/uselessDeta.csv','a+')
outFile.close()
						

inFile.close()


