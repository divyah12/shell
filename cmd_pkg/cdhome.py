#!/usr/bin/python

import os
from os.path import expanduser

def cdhome():
		hf=open("commandoutput.txt","r+")
		open("commandoutput.txt","w").close()
		hf=open("commandoutput.txt","w")
		home = expanduser("~")
		os.chdir(home)
		rtemp=os.getcwd()
		print rtemp
		hf.write(rtemp)
		hf.close()



