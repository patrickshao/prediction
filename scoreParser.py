#Huu Le
#input a text file of scores and outputs results

import string

class ScoreParser:

	"""
	ScoreParser takes in 2 Strings: the name of the input
	file and output file, and a list of strings of team names.

	variables:
	self.inFile    : the input file name
	self.outFile   : the output file name
	self.teamList  : the list of teams
	self.dataTable : the data representation of scores

	Other instance variables are either insignificant or pointless.
	"""
	def __init__(self,ifName,ofName,teamList):
		self.inFile = ifName       #file name for input
		self.outFile = ofName      #file name for output
		self.teamList = teamList   #list of teams, assume ABC order
		self.size = len(teamList)
		self.dataTable = [[0 for x in range(self.size)] for x in range(self.size)]

	"""
	Hashing functions for team name -> index on board and vice versa
	Hash function is simply team name = index in teamList
	Assumes no duplicate teams and teamList is in ABC order
	"""

	def hashToTeam(self,index):
		"""
		Given an index, get the team name
		"""

		#Check for out of bounds error
		if index >= self.size:
			print "Error: index ", index, " is out of bounds for teamList size: ", self.size
			return

		#Get team name
		return self.teamList[index]

	def hashToIndex(self,team):
		"""
		Given a team, get the index
		"""
		#Scan through list for team name
		for x in range(len(self.teamList)):
			t = self.teamList[x]
			if t.lower() == team.lower:
				return x

		#Team name could not be found.
		print "Error: Team Name: \"",team,"\" could not be found within the teamList."
		return


	def fillTableRow(self,rowN,rowLines):
		"""
		Given a a row indicator and the scores for that row,
		transfer the data onto the table
		"""
		
		#Toss away first element - it'll be the team name
		rowLines.pop(0)

		#Iterate through line and fill the row in the table accordingly
		for x in range(len(rowLines)):
			score = rowLines[x]

			#Empty score AKA x = rowN AKA team vs. itself 
			if score == "nil":
				continue

			self.dataTable[rowN][x] = score


	def scanInputFile(self):
		"""
		Scans the input file, takes lines, and process each line
		into the table via fillTableRow()
		"""

		#Grab the list of lines from the input file
		f = open(self.inFile,'r')
		lines = f.readlines()
		f.close

		#First line of file is throwaway, only used for legibility in file
		lines.pop(0)

		#Iterate through each line
		for x in range(len(lines)):
			self.fillTableRow(x,lines[x].split())

	def writeOutputFile(self):
		"""
		Takes the dataTable and then transforms the data
		onto an output file
		"""

		#We ignore the diagonal and start at i+1 to avoid
		#writing duplicate game scores
		f = open(self.outFile, 'w')
		for i in range(len(self.dataTable)):
			for j in range(i+1,len(self.dataTable[i])):
				line = self.hashToTeam(i) + "_" 
				line += self.dataTable[i][j] + "_"
				line += self.hashToTeam(j) +"\n"
				f.write(line)
		f.close()


"""
Testing.... To be removed later
"""
print "Beginning test run...."

teamList = ["Arsenal","Aston Villa","Cardiff City","Chelsea",
			"Crystal Palace","Everton","Fulham","Hull City",
			"Liverpool","Manchester City","Manchester United",
			"Newcastle United","Norwich City","Southampton",
			"Stoke City","Sunderland","Swansea City","Tottenham Hotspur",
			"West Bromwich Albion","West Ham United"]


parser = ScoreParser("data.txt","output.txt",teamList)
parser.scanInputFile()
parser.writeOutputFile()