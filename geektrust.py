import enum
import sys
def main():
    input_file=sys.argv[1]
    f= open(input_file ,"r")
    source=(f.readline().split(' '))#reading file and spliting it based on spaces
    destination=f.readline().split(' ')
    f.close()
    m1=man()#object creation for gman
    m1.source_x_coordinate=int(source[1])
    m1.source_y_coordinate=int(source[2])
    m1.destination_x_coordinate=int(destination[1])
    m1.destination_y_coordinate=int(destination[2])
    m1.initialdirection=m1.matchDirection(source[3])
    if(m1.isInputValid()):
        print('POWER ',m1.computePower())
    else:
        print('OutofBound')
    f.close()

class ToReach(enum.IntEnum):
    North=0
    East=1
    South=2
    West=3
class man:
    source_x_coordinate:int
    source_y_coordinate:int
    initialdirection:int
    destination_x_coordinate:int
    destination_y_coordinate:int
    powerremaining:int=200
    requireddirections=[] 
    def assignvalues(self,source_x_coordinate:int,source_y_coordinate:int,initialdirection:int,destination_x_coordinate:int,destination_y_coordinate:int) :
        self.source_x_coordinate=source_x_coordinate
        self.source_y_coordinate=source_y_coordinate
        self.destination_x_coordinate=destination_x_coordinate
        self.destination_y_coordinate=destination_y_coordinate
        self.initialdirection=initialdirection
        return True       
    def computePower(self):
        iswillingtomovewest = self.destination_x_coordinate-self.source_x_coordinate<0
        iswillingtomovetop = self.destination_y_coordinate-self.source_y_coordinate>0
        iswillingtomovedown = self.destination_y_coordinate-self.source_y_coordinate<0
        if(self.isWillingToMoveEast()):
            self.requireddirections.append(ToReach.East)
        elif(iswillingtomovewest):
            self.requireddirections.append(ToReach.West)
        if(iswillingtomovetop):
            self.requireddirections.append(ToReach.North)
        elif(iswillingtomovedown):
            self.requireddirections.append(ToReach.South)
        self.powerConsumedForTurn()#power consumed for making all turns gets substracted
        self.powerremaining-=self.powerCosumedForMovingAlongXaxies()+self.poweConsumedForMovingAlongYaxies()

        return (self.powerremaining)

    def powerConsumedForTurn(self):
        while(len(self.requireddirections)!=0):
            if(self.initialdirection in self.requireddirections):#if initial direction is matching with required direction
                self.requireddirections.remove(self.initialdirection)
            elif((self.initialdirection+1)%4 in self.requireddirections):#if initial direction is matching with required direction after one trun
                self.powerremaining-=5
                self.requireddirections.remove((self.initialdirection+1)%4)
                self.initialdirection=(self.initialdirection+1)%4
            elif((self.initialdirection+3)%4 in self.requireddirections):#if initial direction is matching with required direction after one turns
                self.powerremaining-=5
                self.requireddirections.remove((self.initialdirection+3)%4)
                self.initialdirection=(self.initialdirection+3)%4
            elif((self.initialdirection+2)%4 in self.requireddirections):#if initial direction is matching with required direction after two trun
                self.powerremaining-=10
                self.requireddirections.remove((self.initialdirection+2)%4)
                self.initialdirection=(self.initialdirection+2)%4
    def poweConsumedForMovingAlongYaxies(self):
        return abs(self.source_y_coordinate-self.destination_y_coordinate)*10

    def powerCosumedForMovingAlongXaxies(self):
        return abs(self.destination_x_coordinate-self.source_x_coordinate)*10

    def isWillingToMoveEast(self):
        return self.destination_x_coordinate-self.source_x_coordinate>0

    def matchDirection(self,sourceDirection:str)->int:
        if(sourceDirection=="N\n"):
            return 0
        elif(sourceDirection=="E\n"):
            return 1 
        elif(sourceDirection=="W\n"):
            return 3
        elif(sourceDirection=="S\n"):
            return 2
    def isInputValid(self):
        if((self.source_x_coordinate<=6 and self.destination_x_coordinate<=6) and (self.destination_y_coordinate<=6 and self.source_y_coordinate<=6)):
            return True
        else:
            return False
if __name__=='__main__':
        main()







    

        