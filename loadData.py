import string
import team
import csv

#Dictionary teamDict[teamname] = team object
teamDict = dict()

#year takes in the whole year parameter
def run(year):
        fname="raw/"+year+" raw.csv"
        #r=open(fname)
        with open(fname,'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                        #Use to print out the row
                        #line = ",".join(row)
                        print row[""],row["AwayTeam"]
                        
                        scores = line.pop(1).split('-')
                        #print line
                        #print scores
                        lTeam = row["HomeTeam"]
                        rTeam = row["AwayTeam"]
                        lScore = scores[0]
                        rScore = scores[1]
                        lTup = (lScore,rScore)
                        rTup = (rScore,lScore)
                        if not lTeam in teamDict.keys():
                                tempTeam = team.makeTeam(lTeam)
                                teamDict[lTeam] = tempTeam
                        if not rTeam in teamDict.keys():
                                tempTeam2 = team.makeTeam(rTeam)
                                teamDict[rTeam] = tempTeam2
                        #print (teamDict[lTeam].scoresDict.keys(),"TSM")
                        if not lTeam in teamDict[lTeam].scoresDict.keys() and not rTeam in teamDict[lTeam].scoresDict.keys():
                                teamDict[lTeam].scoresDict[rTeam] = list()
                                #print "booyah"                 
                        if not rTeam in teamDict[rTeam].scoresDict.keys() and not lTeam in teamDict[rTeam].scoresDict.keys():
                                teamDict[rTeam].scoresDict[lTeam] = list()
                        #print teamDict[lTeam].scoresDict[rTeam]
                        teamDict[lTeam].scoresDict[rTeam].append(lTup)
                        #print teamDict[lTeam].scoresDict[rTeam]
                        teamDict[rTeam].scoresDict[lTeam].append(rTup)
                        teamDict[lTeam].scoresList.append([rTeam,lTup])
                        teamDict[rTeam].scoresList.append([lTeam,rTup])
                        teamDict[lTeam].totalGames+=1 
                        teamDict[rTeam].totalGames+=1
                        if lScore > rScore:
                                teamDict[lTeam].totalWins+=1
                        else:
                                teamDict[rTeam].totalWins+=1
                        if line[2] == "p":
                                teamDict[lTeam].premier = True
                                teamDict[rTeam].premier = True
                        if line[2] == "c":
                                teamDict[lTeam].premier = False
                                teamDict[rTeam].premier = False"""

run("2001")
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
