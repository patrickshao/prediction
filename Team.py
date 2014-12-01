class Team:
	def __init__(self,name):
		self.name = name
		#scoresDict[opposing team] = [(team score, opposing score)...]
		self.scoresDict = dict() 
		#scoresList[chronological by time] = [[team, (team score, opposing score)]...]
		self.scoresList = list()
		self.totalGames = 0
		self.totalWins = 0

	def getRecentGames(self,num):
		temp = list()
		if len(scoresList)-1 > num:
			for i in range(num,len(scoresList)):
				temp.append(scoresList(i))
		return temp

	def historyVs(self,team):
		return scoresDict[team]

