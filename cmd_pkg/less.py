#!/usr/bin/env python
from collections import deque
import os
import shutil

def less(arg):
 hf=open("commandoutput.txt","r+")
 open("commandoutput.txt","w").close()
 hf=open("commandoutput.txt","w")
 if len(arg)==2:
   if(os.path.exists(arg[1])):
	filename=arg[1]
        page_size=10
        d=[];
        d=deque(open(filename))
        if(len(d)<page_size):
                for elem in range(len(d)):
                            print(d[elem])
                print('END')
        else:
             for elem in range(page_size):
                print(d[elem])
             endpoint=page_size
             i=1
             while True:
                   i=i+1
                   next=endpoint
                   endpoint=i*page_size
                   input=raw_input()
                   if(input==""):
                            if(next==len(d)):
                                print(d[next])
                                print('END')
                                break
                            else:
                                if(endpoint<len(d)):
                                     for elem in range(next,endpoint):
                                         print(d[elem])
                                else:
                                     for elem in range(next,len(d)):
                                         print(d[elem])
                                     print('END')
                                     #print("Press ctr+X")
                                     break

                   else:
                        break

   else:
    print("Source file doesn't exists")
 elif len(arg)==4:
    if(os.path.exists(arg[1])):
      if(arg[2]=='>'):
      	shutil.copyfile(arg[1],arg[3])
	#shutil.copyfile(arg[1],"commandoutput.txt")
      elif(arg[2]=='>>'):
	  file =open (arg[3],"a")
          src = open(arg[1], "r")
          for elem in src:
                 file.write(elem+'\n') 
          #shutil.copyfile(arg[1],"commandoutput.txt")
    else:
     print("Source file doesn't exists")
 else:
   print("Invalid arguments, try with spaces between arguments")
 hf.write(filename)
 hf.close() 
		






