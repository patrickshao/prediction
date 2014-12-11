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
        store = 9999
        i = len(self.scoresList)-1
        first = True
        while i >= 0 and num >= 0:
            print self.scoresList[i][4],self.scoresList[i][5],self.scoresList[i][6]
            #print self.scoresList[i][4]
            if self.scoresList[i][5] <= y:
                #3 = d , 4 = m, 5 = y
                #5th day of 3 month of 2012
                #start at 2014, find 2012.
                if self.scoresList[i][4] <= m or not self.scoresList[i][5] == y: 
                #find 3 month
                #find games BEFORE 5th day
                    if self.scoresList[i][3] <=d or not self.scoresList[i][4] == m:
                        if self.scoresList[i][2] == opposing:
                            temp.append(self.scoresList[i])
                            num-=1
                            if first:
                                store = self.scoresList[i+1][0]
                                first = False
                #check if opposing is correct
                #add into list
                #otherwise decrement
            i-=1
        return store,temp

    def historyVs(self,team):
        print "asldkjfsadklf"
        temp = list()
        for teamScore in self.scoresList:
            if teamScore[0] == team:
                temp.append(teamScore[1])
        return temp

    def wins(self,current):
        tempWin = 0
        for r in range(0,current):
            (opponent,scoreTup) = self.scoresList[r]
            (tScore,oScore) = scoreTup
            if tScore > oScore:
                tempWin+=1
        return tempWin
                    
def makeTeam(name):
    team = Team(name)
    return team
