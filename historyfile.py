#!/usr/bin/env python
from cmd_pkg import commands
import threading
import sys
import os
import shutil


def run_command(cmd,args=None,flags=None):
    if args:
        c = threading.Thread(target=cmd, args=(args,))
    else:
        c = threading.Thread(target=cmd)

    c.start()
    c.join()

def call(cmdList):
   i=0
   if(input==""):
        pass
   elif cmdList[i] == 'ls':
		if len(cmdList)<2:
			run_command(commands.ls,cmdList)
		elif len(cmdList)==2 and cmdList[1]=="|":
			run_command(commands.ls,cmdList)
                elif len(cmdList)==3 and cmdList[1]==">":
                        run_command(commands.ls,cmdList)
		else:    
                   run_command(commands.lsa,cmdList)
   elif cmdList[i] == 'cd':
		if len(cmdList)>1 :
			run_command(commands.cd,cmdList)
		else:
			run_command(commands.cdhome)
   elif cmdList[i] == 'pwd':
        run_command(commands.pwd,cmdList)
   elif cmdList[i] =='mkdir':
        run_command(commands.mkdir,cmdList)
   elif cmdList[i] =='rmdir':
        run_command(commands.rmdir,cmdList)
   elif  cmdList[i]== 'cat':
   		if len(cmdList)>4 :
			run_command(commands.catfile,cmdList)
		else:
			run_command(commands.cat,cmdList)
   elif cmdList[i] == 'mv':
        run_command(commands.mv,cmdList)		   
   elif  cmdList[i]== 'grep':
        run_command(commands.grep,cmdList)
   elif cmdList[i] == 'cp':
        run_command(commands.cp,cmdList)
   elif  cmdList[i]== 'rm':
        run_command(commands.rm,cmdList)
   elif cmdList[i] == 'history':
        run_command(commands.history,cmdList)   
   elif  cmdList[i]== 'tail':
        run_command(commands.tail,cmdList)
   elif  cmdList[i]== 'head':
        run_command(commands.head,cmdList)
   elif  cmdList[i]== 'sort':   
        run_command(commands.sort,cmdList)
   elif  cmdList[i]== 'who':
        run_command(commands.who)
   elif  cmdList[i]=='chmod':
        run_command(commands.chmod,cmdList)
   elif	 cmdList[i]== 'less':
        run_command(commands.less,cmdList)
   elif  cmdList[i]== 'wc':
		run_command(commands.wc,cmdList)
   elif  cmdList[i][0]== '!':
		run_command(commands.x,cmdList[0][1:])
		filex=open("tempxhistory.txt","r")
		cx=filex.readline()
		cx=cx.split()
		#print cx
		call(cx)
   else:
        print("command not found")



if __name__ == '__main__':
	cmdList = []
	cmd=[]
	while True:
		print '%',
		input=raw_input()
		if(input=='exit'):
			break
		f = open("historyfile.py", "a")
		f.write(input + '\n')
		if "|" in input:
			piptemp=input.split("|")
                        cmd=piptemp[0].split()
                        cmd.append("|")
                        call(cmd)
			for i in range(1,len(piptemp)):
				f1=open("copyofoutput.txt","r")
				shutil.copyfile("commandoutput.txt","copyofoutput.txt")
				cmd=piptemp[i].split()
				cmd.append("<")
				cmd.append("copyofoutput.txt")
                                cmd.append("|")
                                # print ("root or main ")
				# print cmd
				call(cmd)
                        f2=open("commandoutput.txt","r")
                        lines = f2.readlines()
                        for l in lines:
                           print(l)
		else:
			cmdList= input.split()
			call(cmdList) 





cp driver.py historyfile.py
cat historyfile.py
wc < driver.py
wc driver.py > t1.py
ll
ls
cat textfile.py

wc textfile.py
grep cat textfile.py
cat textfile.py
rm
mkdir
rmdir
ls
cd 
cd ..
cd /hom_group08
cd /home/opsys_group08
cd ..
pwd
cd pwd
cd home/opsys_group08
cd home/opsys_group08
cd
cat driver.py
cd ~
pwd
cd ..
cd /home/opsys_group08
cd ~
cd /home/opsys_group08

ls
mv t1.py t2.py
ls
ls -alh
ls -al
ls -hal
ls -ah
ls -hl
cat textfile.py
less textfile.py
head driver.py
head driver.py
head driver.py > test1.py
grep who < textfile.py
cat textfile.py
grep cat < textfile.py
sort textfile.py
grep less < textfile.py
wc < textfile.py
history
!171
!169
cd ~
who
cat textfile.py
ls
ls-l
ls -al
ls -l
chmod 777 test1.py
ls
ls -l
ls
ls -l
ls -al
ls -lah
mkdir
mkdir sowji
ls
rmdir
rmdir sowji
rmdir sowji
cp driver.py test1.py
cat driver.py
cat test1.py
wc test1.py
wc driver.py
ls
rm test1.py
ls
grep file textfile.py
cat textfile.py
sort textfile.py
grep file textfile.py | sort
grep file textfile.py
sort textfile.py
grep def < driver.py
sort textfile.py > sorted.txt
sort textfile.py > t1.py
ls
sort textfile.txt > t2.py
sort textfile.py > t2.py
cat t2.py
who 
history
!216
ls -l
chmod 777 textfile.py
ls -l
less driver.py
cat textfile.py
cat textfile.py >> textfile.py
cat textfile.py
head driver.py | grep cmdList 
head driver.py | grep cmdList | sort | wc
tail driver.py
tail driver.py | head 
