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

    def getRecentGames(self,num,d,m,y):
        temp = list()
        back = 0
        first = True
        successes = 0
        listLength = len(self.scoresList)
        y = int(y)
        m = int(m)
        d = int(d)-1
        if listLength-1 > num: #useless if statement
            if num > back:
                #temp+=self.scoresList[i][0],self.scoresList[i][6],self.scoresList[i][7]
                #back+=1
                i = listLength-1-back
                while back < num and i >=0:
                    #print self.scoresList[i]
                    mon = int(self.scoresList[i][4])
                    day = int(self.scoresList[i][3]) 
                    yea = int(self.scoresList[i][5])
                    #print "Current",mon,day,yea,"Finding",m,d,y
                    if yea <= y:
                        #print "Passed year"
                        #3 = d , 4 = m, 5 = y
                        #5th day of 3 month of 2012
                        #start at 2014, find 2012.
                        if mon <= m or yea != y:
                            #print "Passed Month" 
                        #find 3 month
                        #find games BEFORE 5th day
                            if day <=d or mon != m or yea != y:
                                #print "Passed day"
                                #Adding the result, game score, and opposing game score
                                #print "Matched"
                                temp+=self.scoresList[i][0],self.scoresList[i][6],self.scoresList[i][7]
                                successes+=1
                                back+=1
                                #if it is the first time, store the value and decrement the date
                                #used so that there is another iteration (currently risks potential
                                #errors in the fact that there could be repeats... need to be fixed)
                    i-=1
            while successes < num:
                temp+=0,0,0
                successes+=1
        #print "------"
        return temp

    def getRecentTotalScores(self,num,d,m,y):
        temp = list()
        back = 0
        first = True
        successes = 0
        listLength = len(self.scoresList)
        y = int(y)
        m = int(m)
        d = int(d)-1
        tScored = 0
        tScoredAgainst = 0
        if listLength-1 > num: #useless if statement
            if num > back:
                #temp+=self.scoresList[i][0],self.scoresList[i][6],self.scoresList[i][7]
                #back+=1
                i = listLength-1-back
                while back < num and i >=0:
                    #print self.scoresList[i]
                    mon = int(self.scoresList[i][4])
                    day = int(self.scoresList[i][3]) 
                    yea = int(self.scoresList[i][5])
                    #print "Current",mon,day,yea,"Finding",m,d,y
                    if yea <= y:
                        #print "Passed year"
                        #3 = d , 4 = m, 5 = y
                        #5th day of 3 month of 2012
                        #start at 2014, find 2012.
                        if mon <= m or yea != y:
                            #print "Passed Month" 
                        #find 3 month
                        #find games BEFORE 5th day
                            if day <=d or mon != m or yea != y:
                                #print "Passed day"
                                #Adding the result, game score, and opposing game score
                                #print "Matched"
                                #temp+=self.scoresList[i][0],self.scoresList[i][6],self.scoresList[i][7]
                                tScored+=int(self.scoresList[i][6])
                                tScoredAgainst+=int(self.scoresList[i][7])
                                successes+=1
                                back+=1
                                #if it is the first time, store the value and decrement the date
                                #used so that there is another iteration (currently risks potential
                                #errors in the fact that there could be repeats... need to be fixed)
                    i-=1
        temp+=tScored,tScoredAgainst
        #print "------"
        return temp

    def currentStats(self,num,d,m,y):
        temp = list()
        back = 0
        first = True
        successes = 0
        listLength = len(self.scoresList)
        y = int(y)
        m = int(m)
        d = int(d)-1
        win = 0.0
        loss = 0.0
        tie = 0.0
        total = 0.0
        if listLength-1 > num: #useless if statement
            if num > back:
                #temp+=self.scoresList[i][0],self.scoresList[i][6],self.scoresList[i][7]
                #back+=1
                i = listLength-1-back
                while back < num and i >=0:
                    #print self.scoresList[i]
                    mon = int(self.scoresList[i][4])
                    day = int(self.scoresList[i][3]) 
                    yea = int(self.scoresList[i][5])
                    #print "Current",mon,day,yea,"Finding",m,d,y
                    if yea <= y:
                        #print "Passed year"
                        #3 = d , 4 = m, 5 = y
                        #5th day of 3 month of 2012
                        #start at 2014, find 2012.
                        if mon <= m or yea != y:
                            #print "Passed Month" 
                        #find 3 month
                        #find games BEFORE 5th day
                            if day <=d or mon != m or yea != y:
                                #print "Passed day"
                                #Adding the result, game score, and opposing game score
                                #print "Matched"
                                #temp+=self.scoresList[i][0],self.scoresList[i][6],self.scoresList[i][7]
                                res = int(self.scoresList[i][0])
                                if res == 2:
                                    win+=1
                                elif res == 1:
                                    tie+=1
                                elif res == 0:
                                    loss+=1
                                total+=1
                                successes+=1
                                back+=1
                                #if it is the first time, store the value and decrement the date
                                #used so that there is another iteration (currently risks potential
                                #errors in the fact that there could be repeats... need to be fixed)
                    i-=1
        if total != 0:
            temp+=win/total,loss/total,tie/total
        else:
            temp+=0,0,0
        #print "------"
        return temp


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
            #hacky way to prevent the mon error, does not read the mon line
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
                    if day <=d or mon != m or yea != y:
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

        #Adding scores of recent five games.
        #temp+=self.getRecentGames(5,d,m,y) 
        #temp+=self.getRecentTotalScores(10,d,m,y) #3 was good
        temp = list()
        temp+=self.currentStats(5,d,m,y)
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
