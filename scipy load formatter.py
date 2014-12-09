#Owen Chapman & Ptrixt@(c)
#formatter

#to do
#map labels to data
#convert all data to numbers
#which labels do we want to use

#read the team names from file
def readTeamList():
    r=open("teamNames.txt")
    tlist=[]
    for line in r:
        line=line.split(',')
        for word in line:
            tlist.append(word)
    r.close()
    return tlist

#read column labels from a year's data
#preprocess for iteration
#return list of strings
def readLabels(r):
    labellist=[]
    for line in r:
        line.strip()
        line=line.split(',')
        for word in line:
            labellist.append(word)
        break
    (labellist[-1])=(labellist[-1][:-1])
    return labellist

#format csv to standardized label order
#convert strings to numbers
def formatData(r,w):
    pass


#main method
def run():
    r=open('2014 raw.csv')
    labellist=readLabels(r)
    print labellist
