class Team:
    def __init__(self,name):
        self.name = name
        #scoresDict[opposing team] = [[result, team, 
        # opposing team, day, month, year, goals scored, opposing goal scored]...]
        self.scoresDict = dict() 
        #scoresList[chronological by time] = [[result, team, opposing team, day, 
        #  month, year, goals scored, opposing score]...]
        self.scoresList = list()
        self.totalGames = 0
        self.totalWins = 0
        self.premier = False

    """def getRecentGames(self,num):
        temp = list()
        if len(self.scoresList)-1 > num:
            for i in range(num,len(self.scoresList)):
                temp.append(self.scoresList(i))
        return temp"""

    def getRecentGamesVS(self,d,m,y,num,opposing):
        temp = list()
        #ensures values are initialized
        label = 9999
        nm = 9999
        nd = 9999
        ny = 9999
        i = len(self.scoresList)-1
        first = True
        #decrements from the back, as well as checking for the
        #number of head to head games planned to record
        while i >= 0 and num > 0:
            #hacky way to prevent the mon error
            if self.scoresList[i][4] == "mon":
                return None
            mon = int(self.scoresList[i][4])
            day = int(self.scoresList[i][3])
            yea = int(self.scoresList[i][5])

            y = int(y)
            m = int(m)
            d = int(d)
            if yea <= y:
                #3 = d , 4 = m, 5 = y
                #5th day of 3 month of 2012
                #start at 2014, find 2012.
                if mon <= m or yea != y: 
                #find 3 month
                #find games BEFORE 5th day
                    if day <=d or mon != m:
                        if self.scoresList[i][2] == opposing and not first:
                            #Adding the result, game score, and opposing game score
                            temp+=self.scoresList[i][0],self.scoresList[i][6],self.scoresList[i][7]
                            num-=1
                            #if it is the first time, store the value and decrement the date
                            #used so that there is another iteration (currently risks potential
                            #errors in the fact that there could be repeats... need to be fixed)
                        elif first:
                            label = self.scoresList[i][0]
                            first = False
                            nm = mon
                            nd = day-1
                            ny = yea
                #check if opposing is correct
                #add into list
                #otherwise decrement
            i-=1
        if not num == 0:
            #print "Not enough data"
            return None
        if label == 9999 or temp == None:
            return None
        return label,temp,nd,nm,ny

    def historyVs(self,team):
        temp = list()
        for teamScore in self.scoresList:
            if teamScore[0] == team:
                temp.append(teamScore[1])
        return temp

    """def wins(self,current):
        tempWin = 0
        for r in range(0,current):
            (opponent,scoreTup) = self.scoresList[r]
            (tScore,oScore) = scoreTup
            if tScore > oScore:
                tempWin+=1
        return tempWin"""
                    
def makeTeam(name):
    team = Team(name)
    return team
