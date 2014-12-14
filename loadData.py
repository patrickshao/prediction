import string
import team
import csv

#Dictionary teamDict[teamname] = team object
teamDict = dict()

def addData(name):
        #fname="alldata.csv"
        #teamDict = dict()
        fname = name
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
def makeCSV(inputName,outputName,day,month,year,numIter,numPast):
    #print "go"	
    with open(outputName, 'w') as csvfile:
        with open(inputName, 'r') as csvfile2:
            #print "go"
            w = csv.writer(csvfile)
            r = csv.reader(csvfile2)
            addData(inputName)
            first = True
            #print "go"
            for row in r:
                if first:
                    first = False
                    continue
                d = row[3]
                m = row[4]
                y = row[5]
                t1 = row[1]
                t2 = row[2]
                team = teamDict[t1]
                gamesList = team.getRecentGamesVS(d,m,y,numPast,t2)
                #print gamesList
                if gamesList != None:
                    w.writerow([gamesList[0]]+gamesList[1])
                    
                #print team1,team2
                #gamesList = makeCSVHelper(inputName,outputName,team1,team2,day,month,year,numIter,numPast)
                #teamDict = dict()
				#makeCSV("validationset.csv","validate.csv",t1,t2,4,3,9999,100,2)
				#teamDict = dict()
				#makeCSV("testingset.csv","test.csv",t1,t2,4,3,9999,100,2)
                """if len(gamesList) != 0:
                    print gamesList
                    for i in range(0,len(gamesList)):
                        if gamesList[i][1] != []:
                            w.writerow([gamesList[i][0]]+gamesList[i][1])"""
                

"""def makeCSVHelper(inputName,outputName,team,opposing,day,month,year,numIter,numPast):
    #addData(inputName)
    #print teamDict
    gamesList = list()
    if team in teamDict.keys():
        teamObj = teamDict[team] 
        #gamesList = teamObj.scoresDict[opposing]
        tm = month
        ty = year
        td = day
        for i in range (0,numIter):
            #currently gets the recent games vs another team
            temp = teamObj.getRecentGamesVS(td,tm,ty,numPast,opposing)
            print "temp",temp
            if not temp == None:
                gamesList.append(temp)
                tm = temp[3]
                ty = temp[4]
                td = temp[2]
                print "changed numbers",tm,ty,td
    return gamesList"""
                    
#inputData = [row["res"],row["team"],row["oteam"],row["day"],row["mon"],row["yea"],row["gs"],row["ogs"]]
                        
def run():
	a = open("train.csv",'w')
	a.close()
	makeCSV("trainingset.csv","train.csv",4,3,9999,2,2)
			#teamDict = dict()
			#makeCSV("validationset.csv","validate.csv",t1,t2,4,3,9999,100,2)
			#teamDict = dict()
			#makeCSV("testingset.csv","test.csv",t1,t2,4,3,9999,100,2)
	

run()	



#makeCSV("trainingset.csv","temp.csv","1","2",4,3,2010,10,5)
#makeCSV("trainingset.csv","temp.csv","1","2",4,3,2010,10,5)
#addData()
#blah = team.makeTeam("blah")
#print blah.name
#print("Testing1")
#addData(7)
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
