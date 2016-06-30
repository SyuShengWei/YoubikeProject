#create a 2D array and initialize every element as 0
ODmatrix = [] 
for i in range (0,183):
	new = []
	for j in range (0,183):
		new.append(0)
	ODmatrix.append(new)

#create a 1D array to store the station name
stationFile = open ('c:/Users/SyuShengWei/Desktop/stations.txt')
stationArray = []
while True:
	theStation = stationFile.readline()
	if theStation == '' :
		break
	else :
		theStation = theStation.strip('\n')
		stationArray.append(theStation)

#define a function to print out ODmatrix 2D array
def printMatrix():
	for i in range (0,183):
		for j in range (0,183):
			print(ODmatrix[i][j],end="")
			print(' ',end="")
		print('\n')

#printMatrix()

#count OD rate
for stationNow in range(0,183,1):
	whichStation = stationNow + 1 
	totalOD = 0
	inFile = open ('c:/Users/SyuShengWei/Desktop/split-by-Ori/'+str(whichStation)+'.csv','r')
	ctr = 0
	while True:
		theLine = inFile.readline()
		ctr += 1
		if theLine == '' : 
			break
		else: 
			judgement = list()
			judgement = theLine.split(',')
			#print(judgement[4])
			if(judgement[4] in stationArray):
				totalOD += 1
				ODmatrix[stationNow][stationArray.index(judgement[4])] += 1
			else:
				print("index =" + str(ctr) + "the station = "+ judgement[4] + "from" +judgement[2])
	totalODrate = 0
	for x in range(0,183,1):
		ODmatrix[stationNow][x] = round(ODmatrix[whichStation-1][x] / totalOD,4) * 100
		totalODrate += ODmatrix[stationNow][x]
		
	print('\n' + str(totalODrate) + ' rouud' + str(stationNow +1))

#output and write
outFile = open('c:/Users/SyuShengWei/Desktop/ODrate.txt','a+')
outFile.write('this file is  total OD rate \n')
outFile.write('for each row(A) -> column(B) means the OD rate form A station to B station \n')
for i in range(0,183,1):
	for j in range(0,183,1):
		outFile.write(str(ODmatrix[i][j]).rjust(5))
		outFile.write(" ")
	outFile.write("\n")
	
#printMatrix()