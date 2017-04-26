#!/usr/bin/python
import os


def grep(temp):
 bool =False
 if(("|" in temp)):
   bool = True
   del temp[len(temp)-1]
# print temp
 hf=open("commandoutput.txt","r+")
 open("commandoutput.txt","w").close()
 hf=open("commandoutput.txt","w") 
 if(os.path.exists(temp[2])):
  if len(temp)<4:
	searchfile = open(temp[2], "r")
	for line in searchfile:
		if temp[1] in line:
		  if(bool):	    
		     hf.write(line)
                  else:
                     print line
                     hf.write(line)
	searchfile.close()
  elif len(temp)==5:
   if temp[3]=='>':
       
	searchfile = open(temp[2], "r")
	writefile = open(temp[4], "w")
	for line in searchfile:
		if temp[1] in line:
			print line
			writefile.write(line)
			hf.write(line)
	searchfile.close()
	writefile.close()
   elif temp[3]=='>>':
	searchfile = open(temp[2], "r")
	writefile = open(temp[4], "a")
	for line in searchfile:
		if temp[1] in line:
			print line
			writefile.write(line)
			hf.write(line)
	searchfile.close()
	writefile.close()
 else:
  if ((temp[2]=='<') and (os.path.exists(temp[3]))):
    searchfile = open(temp[3], "r")
    for line in searchfile:
		if temp[1] in line:
		  if(bool):	    
		    hf.write(line)
                  else:
                    print line
                
    searchfile.close()
	
  else:
	 print("Source file doesn't exists")
    	 
 
 #writefile.close()
 hf.close()






