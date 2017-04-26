#!/usr/bin/python

import shutil
import os
def cp(src):
    if(os.path.exists(src[1])):
	    shutil.copyfile(src[1],src[2])
	    print("copied!!")
    else:
	    print("Source file does not exist")







