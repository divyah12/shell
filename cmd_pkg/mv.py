#!/usr/lib/python
import shutil
import os

def mv(src):
	if os.path.isfile(src[1]):
#checks whether source file exists or not
		os.rename(src[1],src[2])
	else:
		print("source file not found")
			


