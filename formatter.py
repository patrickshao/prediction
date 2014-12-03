#Owen Chapman
#first stab at text parsing

import string
#Premiership
#Championship

#opening files.
def getFiles (read, write):
    """
    read: string of filename to be read from.
    write: string name of file to be written to.

    returns: tuple of files (read,write)
    """
    r=open(read)
    w=open(write,'w')
    return (r,w)

def getPremierTeams(r,leaguename):
    """
    finds the team names of all of the teams participating in the premier league of
    a given year.
    
    r: file object to be read from

    return: list of strings. all of the teams' names.
    """
    start=0
    teams=[]
    for line in r:
        line=line.strip()
        if start==0:
            if line==leaguename:
                start=1
        elif start==1:
            if line=="Round 1":
                start=2
        else:
            if line=="Round 2":
                break
            elif line=='' or line[0]=='[' or line[-1]==']':
                continue
            else:
                wordlist=line.split(' ')
                firstname=""
                scoreindex=0
                for i in range(len(wordlist)):
                    word=wordlist[i]
                    if word=='':
                        continue
                    elif word[0] in string.digits:
                        scoreindex=i
                        break
                    else:
                        firstname+=(word+' ')
                firstname=firstname.strip()
                #print firstname
                teams.append(firstname)
                secondname=""
                for i in range(scoreindex+1,len(wordlist)):
                    word=wordlist[i]
                    if word=='':
                        continue
                    else:
                        secondname+=(word+ ' ')
                secondname=secondname.strip()
                #print secondname
                teams.append(secondname)
    return teams
            
    
#09-10. for testing purposes.
globalteams=['Chelsea','Manchester U','Arsenal','Tottenham','Manchester C','Aston Villa',
       'Liverpool','Everton','Birmingham','Blackburn','Stoke','Fulham','Sunderland',
       'Bolton','Wolverhampton','Wigan','West Ham','Burnley','Hull','Portsmouth']
def parse (r,w,pteams,cteams):
    """
    r: file object to be read from
    w: file object to be written to

    returns void
    """
    count = 0
    regseas=0
    for line in r:
        d=parseline(line,pteams+cteams)
        if d!=None:
            (t1,s,t2)=d
            tag='c'
            if t1 in pteams and t2 in pteams:
                regseas+=1
                tag='p'
            #print t1+'_'+s+'_'+t2+'_'+tag
            w.write(t1+'_'+s+'_'+t2+'_'+tag+'\n')
            count +=1
    print regseas, count

def parseline(line,teamlist):
    """
    line: string line to be parsed
    teamlist: list of strings: valid team names. Should be created prior to calling
        this function. All teams in a given league.

    return: void if not a valid score
            (string team, string score, string team) if valid score.
    """
    line=line.strip()
    wordlist=line.split(" ")
    firstname=""
    scoreindex=0
    for i in range(len(wordlist)):
        word=wordlist[i]
        if word=='':
            continue
        elif word[0] in string.digits:
            scoreindex=i
            break
        else:
            firstname+=(word+' ')
    firstname=firstname.strip()
    #print firstname
    score=(wordlist[scoreindex]).strip()
    if (len(score)<3) or (score[0] not in string.digits) or (score[-1] not in string.digits) or (score[1] != '-'):
        return None
    if firstname not in teamlist:
        return None
    secondname=""
    for i in range(scoreindex+1,len(wordlist)):
        word=wordlist[i]
        if word=='':
            continue
        elif word[0]=='[':
            break
        else:
            secondname+=(word+ ' ')
    secondname=secondname.strip()
    #print secondname
    if secondname not in teamlist:
        return None
    return (firstname,wordlist[scoreindex],secondname)

def getFilePrefix(yr1):
    if yr1<10:
        tdy='0'
    else:
        tdy=''
    tdy+=str(yr1)
    if yr1<9:
        tdyp1='0'
    else:
        tdyp1=''
    tdyp1+=str(yr1+1)
    return (tdy+'-'+tdyp1)

def writeTeams(year):
    prefix=getFilePrefix(year)
    r=open(prefix+" scores.txt")
    w=open(prefix+" teams.txt",'w')
    teams=getPremierTeams(r,'Premiership')
    for team in teams:
        print team
        w.write(team+'\n')
    r.close()
    w.close()
    return teams
    

def run(year):
    pteams=writeTeams(year)
    prefix=getFilePrefix(year)
    fname1=prefix+' scores.txt'
    fname2=prefix+' scores formatted.txt'
    r=open(fname1)
    cteams=getPremierTeams(r,'Championship')
    print cteams
    r.close()
    (r,w)=getFiles(fname1,fname2)
    parse(r,w,pteams,cteams)
    r.close()
    w.close()


