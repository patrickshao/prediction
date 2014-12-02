#Owen Chapman
#first stab at text parsing

import string

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

def getPremierTeams(r):
    """
    finds the team names of all of the teams participating in the premier league of
    a given year.
    
    r: file object to be read from

    return: list of strings. all of the teams' names.
    """
    start=False
    teams=[]
    for line in r:
        line=line.strip()
        if start==False:
            if line=="Round 1":
                start=True
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
def parse (r,w,teams):
    """
    r: file object to be read from
    w: file object to be written to

    returns void
    """
    count = 0
    regseas=0
    for line in r:
        d=parseline(line,teams)
        if line[0]=='_':
            regseas=count
        elif d!=None:
            (t1,s,t2)=d
            print d
            w.write(t1+'_'+s+'_'+t2+'\n')
            count +=1
    print count

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
    if firstname not in teamlist:
        return None
    secondname=""
    for i in range(scoreindex+1,len(wordlist)):
        word=wordlist[i]
        if word=='':
            continue
        else:
            secondname+=(word+ ' ')
    secondname=secondname.strip()
    #print secondname
    if secondname not in teamlist:
        return None
    return (firstname,wordlist[scoreindex],secondname)
        

def run(twoDigitYear):
    if twoDigitYear<10:
        tdy='0'
    else:
        tdy=''
    tdy+=str(twoDigitYear)
    if twoDigitYear<9:
        tdyp1='0'
    else:
        tdyp1=''
    tdyp1+=str(twoDigitYear+1)
    
    (r,w)=getFiles(tdy+'-'+tdyp1+' scores.txt',tdy+'-'+tdyp1+' scores formatted.txt')
    teams=getPremierTeams(r)
    parse(r,w,teams)


