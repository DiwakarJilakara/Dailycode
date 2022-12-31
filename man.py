import enum
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
    n:int
    def readInputFromFile(self):
            f=open('textfile.txt','r')
            source=(f.readline().split(' '))
            destination=f.readline().split(' ')
            self.source_x_coordinate=int(source[0])
            self.source_y_coordinate=int(source[1])
            self.destination_x_coordinate=int(destination[0])
            self.destination_y_coordinate=int(destination[1])
            self.initialdirection=self.matchDirection(source[2])

            
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
            self.powerremaining-=(self.powerConsumedForTurns(ToReach.East))
            self.initialdirection=ToReach.East
        elif(iswillingtomovewest):
            self.powerremaining-=self.powerConsumedForTurns(ToReach.West)
            self.initialdirection=ToReach.West
        if(iswillingtomovetop):
            self.powerremaining-=self.powerConsumedForTurns(ToReach.North)
            self.initialdirection=ToReach.North
        elif(iswillingtomovedown):
            self.powerremaining-=self.powerConsumedForTurns(ToReach.South)
            self.initialdirection=ToReach.South
        self.powerremaining-=self.powerCosumedForMovingAlongXaxies()+self.poweConsumedForMovingAlongYaxies()

        return (200-self.powerremaining)

    def poweConsumedForMovingAlongYaxies(self):
        return abs(self.source_y_coordinate-self.destination_y_coordinate)*10

    def powerCosumedForMovingAlongXaxies(self):
        return abs(self.destination_x_coordinate-self.source_x_coordinate)*10

    def isWillingToMoveEast(self):
        return self.destination_x_coordinate-self.source_x_coordinate>0
    def powerConsumedForTurns(self,requireddirection:int)->int:
        if(self.initialdirection==requireddirection):
            return 0
        elif(self.isAdjacentto(requireddirection)):
            return 5
        elif(self.isOppositeto(requireddirection)):
            return 10
    def isAdjacentto(self,requireddirection):
        if((self.initialdirection+3)%4==requireddirection):
            return True
        elif((self.initialdirection+1)%4==requireddirection):
            return True
        else:
            return False
    def isOppositeto(self,requireddirection):
        if((self.initialdirection+2)%4==requireddirection):
            return True
        else:
            return False
    def matchDirection(self,sourceDirection:str)->int:
        if(sourceDirection=="North\n"):
            return 0
        elif(sourceDirection=="East\n"):
            return 1 
        elif(sourceDirection=="West\n"):
            return 3
        elif(sourceDirection=="South\n"):
            return 2






    

        
