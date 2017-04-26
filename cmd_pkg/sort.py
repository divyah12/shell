#!/usr/bin/python
import os

def sort(argval):
        bool=False
        if("|" in argval):
          bool=True
          del(argval[len(argval)-1])
	hf=open("commandoutput.txt","r+")
	open("commandoutput.txt","w").close()
	hf=open("commandoutput.txt","w")
	if len(argval)>3:
		wfile=open(argval[3],"r+")
		if argval[2] =='>':
		    open(argval[3],"w").close()
		    wfile=open(argval[3],"r+")
        if(len(argval)!=3):	
	 if(os.path.exists(argval[1])):
		sfile = open(argval[1])
		lines = sfile.readlines()
		line=[item.strip() for item in lines]
		line.sort()
		for l in line:
			if len(argval)==2:
			      if(bool):
                                hf.write(l+'\n')
                              else:	
                                print l
				hf.write(l+'\n')
			elif len(argval)==4 and argval[2]=='>':		    
				wfile.write(l+'\n')
				hf.write(l+'\n')
				
			elif len(argval)==4 and argval[2]=='>>':
				wfile=open(argval[3],"a")
				wfile.write(l+'\n')
				hf.write(l+'\n')
				
	 else:
		print(argval[1]+" does not exist")
        else:
          if(os.path.exists(argval[2])):
	        sfile = open(argval[2])
		lines = sfile.readlines()
		line=[item.strip() for item in lines]
		line.sort()
		for l in line:
		    if(bool):
			 hf.write(l+'\n')
                    else:
                       print(l)
          else:
            print(argval[2]+" does not exist")	  
	hf.close()







