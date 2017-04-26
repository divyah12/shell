#!/usr/bin/env python
from collections import deque
import os

def head(arg):
  bool =False
  if(("|" in arg)):
   bool = True
   del arg[len(arg)-1]
 # print arg  
  hf=open("commandoutput.txt","r+")
  open("commandoutput.txt","w").close()
  hf=open("commandoutput.txt","r+")
  if len(arg)==2:
   if(os.path.exists(arg[1])):
	filename=arg[1]
	d=[];
	d=deque(open(filename))
	len1=len(d)/4
	if(len1==0):
	  len1=1	
	for elem in range(len1):
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
	  len1=len(d)/4
	  if(len1==0):
	   len1=1	
	  for elem in range(len1):	    
		file.write(d[elem])
		hf.write(d[elem])
	 elif(arg[2]=='>>'):
          file =open (arg[3],"a")
	  filename=arg[1]
	  d=[];
	  d=deque(open(filename))
	  len1=len(d)/4
	  if(len1==0):
	   len1=1	
	  for elem in range(len1):	    
		file.write(d[elem]+'\n')
		hf.write(d[elem])	 
    else:
      print("Source file doesn't exists")	

  elif len(arg)==3:
      if(os.path.exists(arg[2])):
	filename=arg[2]
	d=[];
	d=deque(open(filename))
	len1=len(d)/4
	if(len1==0):
	  len1=1	
	for elem in range(len1):
             if(bool):	    
		hf.write(d[elem])
             else:
               print(d[elem])
      else:
        print("Source file doesn't exists")
  
  
  hf.close()		






