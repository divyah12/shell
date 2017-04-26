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
        cx=cx.split()#print cx
        call(cx)
   else:
       print("command not found")



if __name__ == '__main__':
    cmdList = []
    cmd=[]
    while True:
        print( '%')
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
                call(cmd)
                f2=open("commandoutput.txt","r")
                lines = f2.readlines()
                for l in lines:
                    print(l)
        else:
            cmdList= input.split()
            call(cmdList) 





