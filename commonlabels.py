#Owen Chapman
#odds analysis

#this script was just to run and check some common variables across our
#data set. i've done it, so we shouldnt need to run this code.

import csv

def findall(rcsv, labellist):
    reader=csv.DictReader(rcsv)
    for row in reader:
        for label in row.keys():
            if label not in labellist:
                labellist.append(label)
        break

def findcommon (rcsv, labellist):
    reader=csv.DictReader(rcsv)
    for row in reader:
        for label in labellist:
            if label not in row.keys():
                labellist.remove(label)
        break

def check(needevery,stillneedevery):
    r=[]
    for i in range(len(needevery)):
        item=needevery[i]
        if item in stillneedevery:
            r.append(item)
    return r

def getoddslist(r):
    keys=[]
    for row in r:
        row=row.strip()
        row=row.split()
        keys.append(row[0])
    return keys

keys=['FTHG','FTAG','HS','AS','HST','AST','HC','AC','HF','AF',"AO","HO",'HY','AY','HR','AR']
oddskeys=['IWH', 'IWD', 'IWA', 'LBH', 'LBD', 'LBA', 'WHH', 'WHD', 'WHA']

#main method
YEAR_START = 2000
YEAR_END = 2013
def run():
    #empty alldata.csv
    alllabels=[]
    for year in range(YEAR_START, YEAR_END+1):
        fname="raw/"+str(year)+" raw.csv"
        with open(fname,'r') as f:
            findall(f, alllabels)
            f.close()
    for year in range(YEAR_START, YEAR_END+1):
        fname="raw/"+str(year)+" raw.csv"
        with open(fname,'r') as f:
            findcommon(f, alllabels)
            f.close()
    #checked that all the keys used are in all of the sets
    #print check(keys,alllabels)

    #checked which odds are in all of our files, stored in oddskeys
##    r=open('betting odds key.txt')
##    oddslist=getoddslist(r)
##    print 'oddslist',oddslist
##    print 'alllist',alllabels
##    print check(oddslist,alllabels)
