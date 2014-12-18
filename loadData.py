import string
import team
import csv

#Dictionary teamDict[teamname] = team object
teamDict = dict()

def addData(name):
        fname = name
        with open(fname,'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                        lTeam = row["team"]
                        rTeam = row["oteam"]
                        lScore = row["gs"]
                        rScore = row["ogs"]
                        inputData = [row["res"],row["team"],row["oteam"],row["day"],row["mon"],row["yea"],row["gs"],row["ogs"],row["sh"],row["osho"],row["st"],row["ost"],]
                        #makes sure if team is not within the dict that
                        #there will be a new key instantiated
                        if not lTeam in teamDict.keys():
                                tempTeam = team.makeTeam(lTeam)
                                teamDict[lTeam] = tempTeam
                        if not rTeam in teamDict.keys():
                                tempTeam2 = team.makeTeam(rTeam)
                                teamDict[rTeam] = tempTeam2
                        #instantiates the scoreDictionary for the opposing team
                        if not lTeam in teamDict[lTeam].scoresDict.keys() and not rTeam in teamDict[lTeam].scoresDict.keys():
                                teamDict[lTeam].scoresDict[rTeam] = list()                 
                        if not rTeam in teamDict[rTeam].scoresDict.keys() and not lTeam in teamDict[rTeam].scoresDict.keys():
                                teamDict[rTeam].scoresDict[lTeam] = list()
                        #inputs data of the team into the dictionary and list
                        teamDict[lTeam].scoresDict[rTeam].append(inputData)
                        teamDict[rTeam].scoresDict[lTeam].append(inputData)
                        teamDict[lTeam].scoresList.append(inputData)
                        teamDict[rTeam].scoresList.append(inputData)
                        #calculates win loss and updates total number of games
                        teamDict[lTeam].totalGames+=1 
                        teamDict[rTeam].totalGames+=1
                        if lScore > rScore:
                                teamDict[lTeam].totalWins+=1
                        else:
                                teamDict[rTeam].totalWins+=1

#input and output are the files that are to be read and written to
#numPast is how many games for every iteration you go back in the past
def makeCSV(inputName,outputName,numPast):
    with open(outputName, 'w') as csvfile:
        with open(inputName, 'r') as csvfile2:
            w = csv.writer(csvfile)
            r = csv.reader(csvfile2)
            #adds initial data into the global variable
            addData(inputName)
            first = True
            for row in r:
                #ignores the first row (not needed w/ hacky way)
                if first:
                    first = False
                    continue
                #team/date is set by the current position within the file
                d = row[3]
                m = row[4]
                y = row[5]
                t1 = row[1]
                t2 = row[2]
                team = teamDict[t1]
                #gets data for recent games for a given date
                gamesList = team.getRecentGamesVS(d,m,y,numPast,t2)
                #adds the label as first value and rest are the features (previous games)
                if gamesList != None:
                    w.writerow([gamesList[0]]+gamesList[1])

                    
#inputData = [row["res"],row["team"],row["oteam"],row["day"],row["mon"],row["yea"],row["gs"],row["ogs"] opposing shots, shots on target,
#opp shots on target, corners,]
                        
def run(comp,numberBack):
    print "Reading Simple Set"
    makeCSV("simpletest.csv","simple.csv",numberBack)
    if comp:
        print "Reading Training Set"
        makeCSV("trainingset.csv","train.csv",numberBack)
        print "Reading Validation Set"
        makeCSV("validationset.csv","validate.csv",numberBack)
        #print "Reading Testing Set"
        #makeCSV("testingset.csv","test.csv",numberBack)
    	

run(True,10)	#2 previous games optimum