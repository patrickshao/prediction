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

#team = the current team
#opposing = the opposition team
#day,month,year are self explanatory
#numIter is the number of times that we generate new iterations
#numPast is how many games for every iteration you go back in the past
def makeCSV(inputName,outputName,day,month,year,numIter,numPast):
    with open(outputName, 'w') as csvfile:
        with open(inputName, 'r') as csvfile2:
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

                    
#inputData = [row["res"],row["team"],row["oteam"],row["day"],row["mon"],row["yea"],row["gs"],row["ogs"]]
                        
def run():
    print "Reading Training Set"
    makeCSV("trainingset.csv","train.csv",4,3,9999,2,2)
    print "Reading Validation Set"
    makeCSV("validationset.csv","validate.csv",4,3,9999,2,2)
    print "Reading Testing Set"
    makeCSV("testingset.csv","test.csv",4,3,9999,2,2)
	

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
