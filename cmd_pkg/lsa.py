#!/usr/bin/python
import os
import sys
import stat
import time
import getpass
import colorama
from colorama import Fore, Back, Style
#import curses
#import colored
#Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.

def get_mode_info(mode, filename):
    perms = "-"
    color = "default"
    link = ""
    if stat.S_ISDIR(mode):
        perms = "d"
        color = Fore.CYAN
    elif stat.S_ISLNK(mode):
        perms = "l"
        color = Fore.BLUE
        link = os.readlink(filename)
        if not os.path.exists(filename):
            color = Fore.RED
    elif stat.S_ISREG(mode):
        if mode & (stat.S_IXGRP | stat.S_IXUSR | stat.S_IXOTH):
            color = Fore.WHITE
        else:
            if filename[0] == '.':
                color =Fore.MAGENTA
            else:
                color = Fore.GREEN

    mode = stat.S_IMODE(mode)

    for who in "USR", "GRP", "OTH":
        for what in "R", "W", "X":
            if mode & getattr(stat, "S_I" + what + who):
                perms = perms + what.lower()
            else:
                perms = perms + "-"

    return (perms, color, link)
#"Permissions", "# Links", "Owner", "Size", "Last Mod", "Name"
def f__Count(folder):
   # "count the number of files in a directory"
	dcount=0
	fcount=0
	for _,dirs,files in os.walk(folder):
		dcount+=len(dirs)
		fcount+=len(files)
        return dcount+fcount-1

def lsa(arg1):
	colorama.init(autoreset=True)
	pipel=False
	if "|" in arg1:
		pipel=True
		del arg1[len(arg1)-1]
	hf=open("commandoutput.txt","r+")
	open("commandoutput.txt","w").close()
	hf=open("commandoutput.txt","r+")
	lscomb=["-l","-al","-la","-hl","-lh","-lah","-lha","-hla","-hal","-alh","-ahl"]
	if len(arg1)>2 :
		file=open(arg1[3],"w")
	if (arg1[1] in lscomb ):
		x=f__Count(os.getcwd())
		if len(arg1)==2:
			if (pipel):
				hf.write("Total = "+str(x))
				print "hf write"
			else:
				print "Total = ",x
		if len(arg1)>3:
			file.write("Permissions nlink Owner Size mtime Name\n")
		else:
			if pipel:
				hf.write("Permissions nlink Owner Size mtime Name\n")
			#else:				print "Permissions,nlink,Owner,Size,mtime,Name"
		for f_dir in os.listdir(os.getcwd()):
			info =os.lstat(f_dir)
			nlink = info.st_nlink 
			ts = info.st_mtime
			perms, color, link = get_mode_info(info.st_mode, f_dir)
			time_str = time.strftime("%b %d %Y %H:%M:%S", time.gmtime(ts))
			size = info.st_size
			filenameStr = color+ f_dir
			if link:
				filenameStr += " -> "
			filenameStr += link
			if len(arg1)==2 and not pipel:
				print perms,nlink,getpass.getuser(),size,time_str,filenameStr
			if len(arg1)==2 and pipel:
				hf.write(perms+" "+str(nlink)+" "+getpass.getuser()+"\t"+str(size)+"\t"+time_str+"\t"+filenameStr+"\n")	
			if len(arg1)>3 :
				file.write(perms+" "+str(nlink)+" "+getpass.getuser()+"\t"+str(size)+"\t"+time_str+"\t"+filenameStr+"\n")
					
				
	elif(arg1[1]=='-a'):
		
		for f_dir in os.listdir(os.getcwd()):
			if len(arg1)>3:
				file.write(f_dir+"\n")
			else:
				if pipel:
					hf.write(f_dir+"\t")
				else:
					print f_dir+"\t",
		print(" ")
				
	elif(arg1[1]=='-h' or arg1[1]=='-ah' or arg1[1]=='-ha'):
	  for f_dir in os.listdir(os.getcwd()):
	    if not f_dir.startswith("."):
	     if os.path.isfile(f_dir):
                   if len(arg1)>3:
                     file.write(f_dir+"\n")
                   else:
		       if(pipel):
		          hf.write(f_dir+"\n")
	               else:
                          print Fore.GREEN + f_dir + "  ",
                          hf.write(f_dir+"\n")		   
	     elif os.path.isdir(f_dir):
		  if len(arg1)>3:
                     file.write(f_dir+"\n")
                  else:
		       if(pipel):
		          hf.write(f_dir+"\n")
	               else:
                          print Fore.CYAN + f_dir + "  ",
                          hf.write(f_dir+"\n")

	     else:
		  if len(arg1)>3:
                     file.write(f_dir+"\n")
                  else:
		       if(pipel):
		          hf.write(f_dir+"\n")
	               else:
                          print Fore.BLUE + f_dir + "  ",
                          hf.write(f_dir+"\n")
	  print(" ")		
	else:
		print "sorry!, only -l,-h & -a are implemented"
	hf.close()
	







