#Owen Chapman
#first stab at text parsing

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


def parse (r,w):
    """
    r: file object to be read from
    w: file object to be written to

    returns void
    """
    for line in r:
        line=line.strip()
        wordlist = line.split(" ")
        if wordlist != ['']:
            #____ indicates the end of the readable file
            if wordlist[0][0]=='_':
                print "end: ",line
                break
            elif line[0]=='[' or line[-1]==']':
                continue
            elif wordlist[0]=='Round':
                continue
            else:
                printlist=[]
                for word in wordlist:
                    if word!='':
                        printlist.append(word)
                        w.write(word+' ')
                w.write('\n')
                #print printlist
                

def run():
    (r,w)=getFiles('09-10 scores.txt','09-10 scores formatted.txt')
    parse(r,w)

run()
