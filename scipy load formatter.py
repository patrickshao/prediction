#Owen Chapman & Ptrixt@(c)
#formatter

#to do
#map labels to data
#convert all data to numbers
#which labels do we want to use
import string
import csv

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

#starting features needed: ht index, at index, ht goals, at goals, ft result (label)
#some necessary data structures
FTRhdict={'H':'2','D':'1','A':'0'}
FTRadict={'H':'0','D':'1','A':'2'}
r=open('teamNames.txt')
teamlist=[]
for line in r:
    line=line.strip()
    words=line.split(',')
    teamlist=words
    break
keys=['FTHG','FTAG','HS','AS','HST','AST','HHW','AHW','HC','AC','HF','AF',
      'HO','AO','HY','AY','HR','AR']

#format csv to standardized label order
#convert strings to numbers
def formatData(rcsv,wcsv):
    reader=csv.DictReader(rcsv)
    writer=csv.writer(wcsv)
    error=False
    for row in reader:
        writelist=[]#list of strings to write to the file.
        awritelist=[]

        #format result
        # Home win =2, tie=1, home loss=0
        result=row['FTR']
        writelist.append(FTRhdict[result])
        awritelist.append(FTRadict[result])

        #format team names
        h=None
        a=None
        for i in range(len(teamlist)):
            if row['HomeTeam'] == teamlist[i]:
                h=i
            elif row['AwayTeam'] == teamlist[i]:
                a=i
            if a!=None and h!=None:
                break
        if a==None or h==None:
            error=True
            break
        writelist.append(str(h))
        writelist.append(str(a))
        awritelist.append(str(a))
        awritelist.append(str(h))
        
        #format date
        date= row['Date']
        date=date.strip()
        date=date.split('/')
        for item in date:
            writelist.append(item)
            awritelist.append(item)

        #write league
        #0 indicates premier
        #writelist.append('0')

        #write goals scored
        writelist.append(row['FTHG'])
        writelist.append(row['FTAG'])
        awritelist.append(row['FTAG'])
        awritelist.append(row['FTHG'])

        #write shots, shots on target, shots on woodwork
        #writelist.append(row['HS'])

        #write
        print writelist
        writer.writerow(writelist)
        writer.writerow(awritelist)
            

            
                


#main method
def run(year):
    fname="raw/"+str(year)+" raw.csv"
    with open(fname,'r') as f:
        with open('alldata.csv','w') as g:
            formatData(f,g)
    #labellist=readLabels(r)
    #print labellist