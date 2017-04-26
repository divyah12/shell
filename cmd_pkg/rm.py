#!/usr/bin/python

import os

def rm(file):
    if(len(file)>=2):
        path=file[1]
        if not os.path.exists(path):
            print("No Such file!!")
        else:
	    os.remove(file[1])
            print("success!!")
    else:
	    print("missing operand")




