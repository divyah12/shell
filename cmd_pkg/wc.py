from collections import Counter
from collections import deque
import os
def wc(argval):
    bool = False
    if("|" in argval):
       bool = True
       del argval[len(argval)-1] 
    hf=open("commandoutput.txt","r+")
    open("commandoutput.txt","w").close()
    hf=open("commandoutput.txt","w") 
    numoflines = 0
    numofwords = 0
    numofchars = 0
    if len(argval)==2 and os.path.exists(argval[1]):
        filename=argval[1]
        fname = filename
        with open(fname, 'r') as f:
            for line in f:
             if not line.isspace():
                words = line.split()
                numoflines += 1
                numofwords += len(words)
                numofchars += len(line)
        if(bool):
           hf.write("line count= %d, word count= %d, charcount= %d"%(numoflines,numofwords,numofchars))
        else:
           print("line count= %d, word count= %d, charcount= %d, filename=%s"%(numoflines,numofwords,numofchars,filename))	
	   hf.write("line count= %d, word count= %d, charcount= %d"%(numoflines,numofwords,numofchars))
	hf.close()
    elif len(argval)==3 and os.path.exists(argval[2]):
        filename=argval[2]
        #print "wc soemthing"
        fname = filename
        with open(fname, 'r') as f:
            #print "wc soemthing2"
            for line in f:
              if not line.isspace():
                words = line.split()
                numoflines += 1
                numofwords += len(words)
                numofchars += len(line)
        if(bool):
          hf.write("line count= %d, word count= %d, charcount= %d"%(numoflines,numofwords,numofchars))
        else:
          print("line count= %d, word count= %d, charcount= %d, filename=%s"%(numoflines,numofwords,numofchars,filename))
	hf.close()
    else:
        print("source file not found")






