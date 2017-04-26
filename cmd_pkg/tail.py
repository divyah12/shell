#!/usr/bin/env python
from collections import deque
import os

def tail(arg):
  bool =False
  if(("|" in arg)):
   bool = True
   del arg[len(arg)-1]
 # print arg 
  hf=open("commandoutput.txt","r+")
  open("commandoutput.txt","w").close()
  hf=open("commandoutput.txt","w")
  if len(arg)==2:
   if(os.path.exists(arg[1])):
	filename=arg[1]
	d=[];
	d=deque(open(filename))
	len1=(len(d)*3/4)
	if (len1<1):
	 len1=0;
	elif(len1==1):
         len1=1
	elif(len1==2):
         len1=1
	elif(len1==3):
         len1=2	 
	else:
         len1=len1+1      	
	for elem in range(len1,len(d)):	    
	      if(bool):	    
		hf.write(d[elem])
              else:
                print(d[elem])
                hf.write(d[elem])
   else:
      print("Source file doesn't exists")
  elif len(arg)==4:
    if(os.path.exists(arg[1])):
	 if(arg[2]=='>'):
          file =open (arg[3],"w")
	  filename=arg[1]
	  d=[];
	  d=deque(open(filename))
	  len1=(len(d)*3/4)
	  if (len1<1):
	     len1=0;
	  elif(len1==1):
             len1=1
	  elif(len1==2):
	     len1=1
	  elif(len1==3):
             len1=2	 
	  else:
             len1=len1+1      	
	     for elem in range(len1,len(d)):	    
		    file.write(d[elem])
		    hf.write(d[elem])
         elif(arg[2]=='>>'):
	  file =open (arg[3],"a")
	  filename=arg[1]
	  d=[];
	  d=deque(open(filename))
	  len1=(len(d)*3/4)
	  if (len1<1):
	     len1=0;
	  elif(len1==1):
             len1=1
	  elif(len1==2):
	     len1=1
	  elif(len1==3):
             len1=2	 
	  else:
             len1=len1+1      	
	     for elem in range(len1,len(d)):	    
		    file.write(d[elem]+'\n')
		    hf.write(d[elem])
    else:
      print("Source file doesn't exists")
  elif len(arg)==3:
   if(os.path.exists(arg[2])):
	filename=arg[2]
	d=[];
	d=deque(open(filename))
	len1=(len(d)*3/4)
	if (len1<1):
	 len1=0;
	elif(len1==1):
         len1=1
	elif(len1==2):
         len1=1
	elif(len1==3):
         len1=2	 
	else:
         len1=len1+1      	
	for elem in range(len1,len(d)):	    
	      if(bool):	    
		hf.write(d[elem])
              else:
                print(d[elem])
                
   else:
      print("Source file doesn't exists")	  
  else:
      print("Invalid arguments, try with spaces between arguments")
  hf.close()
  






