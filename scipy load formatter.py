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
#some necessary dictionaries
FTRdict={'H':'2','D':'1','A':'0'}

#format csv to standardized label order
#convert strings to numbers
def formatData(rcsv,wcsv):
    reader=csv.DictReader(rcsv)
    for row in reader:
        error=False
        writelist=[]#list of strings to write to the file.

        #format result
        # Home win =2, tie=1, home loss=0
        result=row['FTR']
        writelist.append(FTRdict[result])
        
        #format date
        date= row['Date']
        date=date.strip()
        date=date.split('/')
        for item in date:
            writelist.append(item)

        #write league
        #0 indicates premier
        writelist.append('0')

        #write goals scored
        writelist.append(str(row['FTHG']))
        writelist.append(str(row['FTAG']))
        
        print writelist

            
                


#main method
def run(year):
    fname="raw/"+str(year)+" raw.csv"
    with open(fname,'r') as f:
        formatData(f,3)
    #labellist=readLabels(r)
    #print labellist
