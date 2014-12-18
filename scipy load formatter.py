#Owen Chapman & Ptrixt@(c)
#formatter

#to do
#map labels to data
#convert all data to numbers
#which labels do we want to use
import string
import csv

#read the team names from file
def readTeamList(filename):
    r=open(filename)
    tlist=[]
    for line in r:
        line=line.strip()
        words=line.split(',')
        tlist=words
        break
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
eplteamfile='teamNames.txt'
spateamfile='spainteamNames.txt'
eteamlist=readTeamList(eplteamfile)
steamlist=readTeamList(spateamfile)
keys=['FTHG','FTAG','HS','AS','HST','AST','HC','AC','HF','AF',
      'HY','AY','HR','AR']
completekeys=['res','team','oteam','day','mon','yea','gs','ogs','sh','osho',
              'st','ost','co','oco','fo','ofo','ye','oye','re','ore']
#[result, team, opposing team, day, month, year, goals scored, opposing goals scored, shots, opposing shots, shots on target,
#opp shots on target, corners, opp corners, fouls, opp fouls, yellow cards, opp yellow cards, red cards, opp red cards]
oddskeys=['IWH', 'IWD', 'IWA', 'LBH', 'LBD', 'LBA', 'WHH', 'WHD', 'WHA']

#format csv to standardized label order
#convert strings to numbers
def formatData(rcsv,wcsv,teamlist):
    reader=csv.DictReader(rcsv)
    writer=csv.writer(wcsv)
    writer.writerow(completekeys)
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
##        if a==None or h==None:
##            error=True
##            break
        if a==None:
            error=row['AwayTeam']
            break
        elif h==None:
            error=row['HomeTeam']
            break
        add(writelist,awritelist,str(h),str(a))
##        writelist.append(str(h))
##        writelist.append(str(a))
##        awritelist.append(str(a))
##        awritelist.append(str(h))
        
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
        add(writelist,awritelist,row['FTHG'],row['FTAG'])

        #write shots, shots on target, corners, fouls, yellows, reds
        add(writelist,awritelist,row['HS'],row['AS'])
        add(writelist,awritelist,row['HST'],row['AST'])
        add(writelist,awritelist,row['HC'],row['AC'])
        add(writelist,awritelist,row['HF'],row['AF'])
        add(writelist,awritelist,row['HY'],row['AY'])
        add(writelist,awritelist,row['HR'],row['AR'])

        #write
        #print writelist
        writer.writerow(writelist)
        writer.writerow(awritelist)
    if error != False:
        print row['HomeTeam'],row['AwayTeam'],date

def add(hlist,alist,hitem,aitem):
    hlist.append(hitem)
    hlist.append(aitem)
    alist.append(aitem)
    alist.append(hitem)
            
#main method
YEAR_TRAINING = (2000,2009)
YEAR_VALIDATION = (1910,1914)
YEAR_TESTING = (2010,2014)
YEAR_END = 2014
def write(filename, startyear, endyear,tlst):
    #empty alldata.csv
    w=open(filename,'w')
    w.close()
    
    with open(filename,'a') as g:
        for year in range(startyear, endyear+1):
            print "doing year", year
            fname="raw/"+str(year)+" raw.csv"
            with open(fname,'r') as f:
                formatData(f,g,tlst)
                f.close()    
    g.close()


def run():
    write('trainingset.csv',YEAR_TRAINING[0],YEAR_TRAINING[1],eteamlist)
    write('validationset.csv',YEAR_VALIDATION[0],YEAR_VALIDATION[1],steamlist)
    write('testingset.csv',YEAR_TESTING[0],YEAR_TESTING[1],eteamlist)
    #labellist=readLabels(r)5
    #print labellist
