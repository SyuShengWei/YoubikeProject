def  ReadOD (filename,Record_List,station_num,peroid_num):
	Output_List = list()
	for O in range(0,station_num):
		O_List = list()
		for D in range(0,station_num):
			D_List = list()
			for peroid in range(0,peroid_num):
				peroid_data = 0
				D_List.append(peroid_data)
			O_List.append(D_List)
		Output_List.append(O_List)
	
	inFile = open(filename,'r')
	Data_List = inFile.readlines()
	for peroid in range(0,peroid_num) :
		One_Peroid_List = Data_List[peroid].strip('\n') # O1D1,O1D2 .... :O2D1,O2D2...:		
		One_O_List = One_Peroid_List.split(':')   # ['O1D1,O1D2','O2D1,O2D2']
		for O in range(0,station_num):
			One_OD_Data = One_O_List[O].split(',')
			for D in range(0,station_num):
				Output_List[O][D][peroid] = int(One_OD_Data[D])
		

#def ReadTotal