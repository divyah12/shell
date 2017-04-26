#!/usr/bin/python

import os

def chmod(file):
    if(os.path.exists(file[2])):
	      os.chmod(file[2],int(file[1],8))
    else:
          print(" source file does not exist") 





