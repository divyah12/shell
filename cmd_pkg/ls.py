#!/usr/bin/python
import os
import colorama
from colorama import Fore

def ls(arg):
        colorama.init(autoreset=True)
        bool =False
        if(len(arg)==1):
	 pass
        elif arg[1]=='>':
         file=open(arg[2],"w")
        if(("|" in arg)):
           bool = True
           del arg[len(arg)-1]
        #mk arg 
	hf=open("commandoutput.txt","r+")
	open("commandoutput.txt","w").close()
	hf=open("commandoutput.txt","w")
	for f_dir in os.listdir(os.getcwd()):
	  if not f_dir.startswith("."):
	     if os.path.isfile(f_dir):
		   if(len(arg)>2):
                     file.write(f_dir+"\n")
                     hf.write(f_dir+"\n")
                   else:
                     if(bool):
		       hf.write(f_dir+"\n")
	             else:
                       print Fore.GREEN + f_dir + "  ",
                       hf.write(f_dir+"\t")		   
             elif os.path.isdir(f_dir):
		 if (len(arg)>2):
                     file.write(f_dir+"\n")
                     hf.write(f_dir+"\n")
                 else:
                    if(bool):
		       hf.write(f_dir+"\n")
	            else:
                       print Fore.CYAN + f_dir + "  ",
		       hf.write(f_dir+"\t")
             else:
                  if (len(arg)>2):
                     file.write(f_dir+"\n")
                     hf.write(f_dir+"\n")
                  else:
		    if(bool):
		      hf.write(f_dir+"\n")
	            else:
                      print Fore.BLUE+f_dir+" ",
		      hf.write(f_dir+"\t")
         
	print(" ")



