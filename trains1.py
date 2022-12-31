class TrainJourney1:
    Train_A=['chn','slm','blr','krn','hyb','ngp','itj','bpl','aga','ndl']
    Train_A_distance={'chn':0,'slm':350,'blr':550,'krn':900,'hyb':1200,'ngp':1600,'itj':1900,'bpl':2000,'aga':2500,'ndl':2700 }
    Train_B=['tvc','srr','maq','mao','pne','hyb','ngp','itj','bpl','pta','njp','ghy']
    Train_B_distance={'tvc':0,'srr':300,'maq':600,'mao':1000,'pne':1400,'hyb':2000,'ngp':2400,'itj':2700,'bpl':2800,'pta':3800,'njp':4200,'ghy':4700}
    Train_A_input=[]
    Train_B_input=[]
    Train_A_Arrival=[]
    Train_B_Arrival=[]
    TrainAB_Final=[]
    '''def TrainInfo(self):
        Train_A=[]
        Train_AB=[]
        Train_B=[]
        Train_A+=self.detach_Boggies_of_TrainA()
        Train_B+=self.detach_Boggies_of_TrainB()
        Train_AB+=self.TrainAB_status()
        return Train_AB'''
    def set_values(self,Train_A_input,Train_B_input):
        self.Train_A_input+=Train_A_input
        self.Train_B_input+=Train_B_input
    def detach_Boggies_of_TrainA(self):
        for i in range(len(self.Train_A_input)):
            if self.Train_A_input[i] in self.Train_A[5:]:
                self.Train_A_Arrival.append(self.Train_A_input[i])
        return self.Train_A_Arrival
    def detach_Boggies_of_TrainB(self):
        for i in range(len(self.Train_B_input)):
            if self.Train_B_input[i] in self.Train_B[6:]:
                self.Train_B_Arrival.append(self.Train_B_input[i])
        return self.Train_B_Arrival
    def TrainAB_status(self):
        self.detach_Boggies_of_TrainB()
        self.detach_Boggies_of_TrainA()
        i=0
        k=len(self.Train_A_Arrival)-1
        l=len(self.Train_B_Arrival)-1
        if(k==-1 and l==-1 ):
            print("JOURENY_ENDED")
            return 'JOURNEY_ENDED'
        while(i<len(self.Train_A_Arrival)+len(self.Train_B_Arrival)):
            if(self.Train_B_distance[self.Train_B_Arrival[l]]>=self.Train_A_distance[self.Train_A_Arrival[k]]):
                self.TrainAB_Final.append(self.Train_B_Arrival[l])
                i+=1
                l-=1
            else:
                self.TrainAB_Final.append(self.Train_A_Arrival[k])
                i+=1
                k-=1
        return self.TrainAB_Final
    def sortBasedONDistanceForTrain_A(self,e:str):
        return self.Train_A_distance[e]
    def sortBasedONDistanceForTrain_B(self,e):
        return self.Train_B_distance[e]
    def trainAArrivalStatus(self):
        return self.Train_A_Arrival
    def trainBArrivalStatus(self):
        return self.Train_B_Arrival


