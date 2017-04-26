#!/usr/lib/python

def history(cmdarg):
    bool =False
    if(("|" in cmdarg)):
       bool = True
       del cmdarg[len(cmdarg)-1]
    #print cmdarg  
    hf1=open("commandoutput.txt","r+")
    open("commandoutput.txt","w").close()
    hf1=open("commandoutput.txt","r+")
    if len(cmdarg)<2:
     hf=open("historyfile.py","r")
     lines=hf.readlines()
     count=0
     for l in lines:
    	count=count+1
        if(bool):
         hf1.write('{} {}'.format(count,l))
	else:
	 print '{} {}'.format(count,l)
    elif len(cmdarg)>2:
     if(cmdarg[1]=='>'):
      file =open (cmdarg[2],"w")
      hf=open("historyfile.py","r")
      lines=hf.readlines()
      count=0
      for l in lines:
       count=count+1
       file.write(str(count)+" "+str(l))
     elif(cmdarg[1]=='>>'):
      file =open (cmdarg[2],"a")
      hf=open("historyfile.py","r")
      lines=hf.readlines()
      count=0
      for l in lines:
       count=count+1
       file.write(str(count)+" "+str(l))
     elif(cmdarg[1]=='<'):	
      hf=open("historyfile.py","r")
      lines=hf.readlines()
      count=0
      for l in lines:
    	count=count+1
        if(bool):
         hf1.write('{} {}'.format(count,l))
	else: 
         print '{} {}'.format(count,l) 
    else:
      print("type command as history(space)>(space)filename")



