import string
import team
import csv

#Dictionary teamDict[teamname] = team object
teamDict = dict()

def run():
        fname="alldata.csv"
        #r=open(fname)
        with open(fname,'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                        #print line
                        #print scores
                        lTeam = row["team"]
                        rTeam = row["oteam"]
                        lScore = row["gs"]
                        rScore = row["ogs"]
                        inputData = [row["res"],row["team"],row["oteam"],row["day"],row["mon"],row["yea"],row["gs"],row["ogs"]]
                        if not lTeam in teamDict.keys():
                                tempTeam = team.makeTeam(lTeam)
                                teamDict[lTeam] = tempTeam
                        if not rTeam in teamDict.keys():
                                tempTeam2 = team.makeTeam(rTeam)
                                teamDict[rTeam] = tempTeam2
                        if not lTeam in teamDict[lTeam].scoresDict.keys() and not rTeam in teamDict[lTeam].scoresDict.keys():
                                teamDict[lTeam].scoresDict[rTeam] = list()                 
                        if not rTeam in teamDict[rTeam].scoresDict.keys() and not lTeam in teamDict[rTeam].scoresDict.keys():
                                teamDict[rTeam].scoresDict[lTeam] = list()
                        teamDict[lTeam].scoresDict[rTeam].append(inputData)
                        teamDict[rTeam].scoresDict[lTeam].append(inputData)
                        teamDict[lTeam].scoresList.append(inputData)
                        teamDict[rTeam].scoresList.append(inputData)
                        teamDict[lTeam].totalGames+=1 
                        teamDict[rTeam].totalGames+=1
                        if lScore > rScore:
                                teamDict[lTeam].totalWins+=1
                        else:
                                teamDict[rTeam].totalWins+=1
                        """if line[2] == "p":
                                teamDict[lTeam].premier = True
                                teamDict[rTeam].premier = True
                        if line[2] == "c":
                                teamDict[lTeam].premier = False
                                teamDict[rTeam].premier = False"""

#team = the current team
#opposing = the opposition team
#day,month,year are self explanatory
#numIter is the number of times that we generate new iterations
#numPast is how many games for every iteration you go back in the past
def makeCSV(team,opposing,day,month,year,numIter,numPast):
        with open('temp.csv', 'wb') as csvfile:
                run()
                teamObj = teamDict[team] 
                #gamesList = teamObj.scoresDict[opposing]
                tm = month
                ty = year
                td = day
                gamesList = list()
                for i in range (0,numIter):
                        #currently gets the recent games vs another team
                        temp = teamObj.getRecentGamesVS(td,tm,ty,numPast,opposing)
                        gamesList.append(temp)
                        tm = temp[3]
                        ty = temp[4]
                        td = temp[2]

                w = csv.writer(csvfile, delimiter=',')
                for i in range(0,len(gamesList)):
                        w.writerow([gamesList[i][0]]+gamesList[i][1])
                        
#inputData = [row["res"],row["team"],row["oteam"],row["day"],row["mon"],row["yea"],row["gs"],row["ogs"]]
                        

makeCSV("1","2",4,3,2010,10,5)
#run()
#blah = team.makeTeam("blah")
#print blah.name
#print("Testing1")
#run(7)
#print teamDict["Chelsea"].wins(4)
#print teamDict["Chelsea"].historyVs("Arsenal")
#print "----------------------------------"
#for name in teamDict:
#	team = teamDict[name]
#	print team.name
#	print team.scoresDicts
#	print team.scoresList
#	print team.totalGames
#	print team.totalWins
