import string
import team


teamList = dict()

def run(year):
	if year<10:
		tdy='0'
	else:
		tdy=''
	tdy+=str(year)
	if year<9:
		tdyp1='0'
	else:
		tdyp1=''
	tdyp1+=str(year+1)
	fname2=tdy+'-'+tdyp1+' scores formatted.txt'
	r=open(fname2)
	for line in r:
		line=line.strip()
		line = line.split('_')
		scores = line.pop(1).split('-')
		#print line
		#print scores
		lTeam = line[0]
		rTeam = line[1]
		lScore = scores[0]
		rScore = scores[1]
		lTup = (lScore,rScore)
		rTup = (rScore,lScore)
		if not lTeam in teamList.keys():
			tempTeam = team.makeTeam(lTeam)
			teamList[lTeam] = tempTeam
		if not rTeam in teamList.keys():
			tempTeam2 = team.makeTeam(rTeam)
			teamList[rTeam] = tempTeam2
		if not lTeam in teamList[lTeam].scoresDict.keys():
			teamList[lTeam].scoresDict[rTeam] = list()			
		if not rTeam in teamList[rTeam].scoresDict.keys():
			teamList[rTeam].scoresDict[lTeam] = list()			
		teamList[lTeam].scoresDict[rTeam].append(lTup)
		teamList[rTeam].scoresDict[lTeam].append(rTup)
		teamList[lTeam].scoresList.append([rTeam,lTup])
		teamList[rTeam].scoresList.append([lTeam,rTup])
		teamList[lTeam].totalGames+=1 
		teamList[rTeam].totalGames+=1
		if lScore > rScore:
			teamList[lTeam].totalWins+=1
		else:
			teamList[rTeam].totalWins+=1


blah = team.makeTeam("blah")
print blah.name
print("Testing")
run(9)

print "----------------------------------"
for name in teamList:
	team = teamList[name]
	print team.name
	print team.scoresDict
	print team.scoresList
	print team.totalGames
	print team.totalWins