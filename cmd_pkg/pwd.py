#!/usr/bin/python
import os

def pwd(cmdList):
	hf=open("commandoutput.txt","r+")
	open("commandoutput.txt","w").close()
	hf=open("commandoutput.txt","w")
	ft=open("temppipe.txt","r+")
	open("temppipe.txt","w").close()
	hf=open("temppipe.txt","w")
	if not '|' in cmdList:
		print(os.getcwd())
	else:
		hf.write(os.getcwd())
		ft.write(os.getcwd())
		ft.close()
		hf.close()




