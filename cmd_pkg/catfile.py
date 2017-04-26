#!/usr/bin/env python
from collections import deque
import os

def catfile(filearg):
  if(os.path.exists(filearg[1])):
	 hf=open("commandoutput.txt","r+")
	 open("commandoutput.txt","w").close()
	 hf=open("commandoutput.txt","w")
	 hf.write(filearg[4])
	 tempfile=[]
	 if(filearg[3]=='>'):
		f1=open(filearg[1])
		f2=open(filearg[2])
		tempfile.append(f1)
		tempfile.append(f2)
		f = open(filearg[4], "w")
		for temp in tempfile:
			for line in temp.readlines():
				f.write(line)
				#hf.write(line)
         elif(filearg[3]=='>>'):
                f1=open(filearg[1])
		f2=open(filearg[2])
		tempfile.append(f1)
		tempfile.append(f2)
		f = open(filearg[4], "a")
		for temp in tempfile:
			for line in temp.readlines():
				f.write(line+'\n')
				#hf.write(line)
	 hf.close()
  else:
     print(" source file does not exist")







