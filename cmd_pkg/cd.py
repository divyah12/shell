 

import os
from os.path import expanduser

def cd(arg):
	hf=open("commandoutput.txt","r+")
	open("commandoutput.txt","w").close()
	hf=open("commandoutput.txt","w")
	path= arg[1]
	if path =='..':
		os.chdir(os.path.dirname(os.getcwd()))
		rss=os.getcwd()
		print rss
                os.chdir("/home/opsys_group08")
		hf.write(rss)
	elif path=='~':
		home = expanduser("~")
		os.chdir(home)
		rtemp=os.getcwd()
		print rtemp
                os.chdir("/home/opsys_group08")
		hf.write(rtemp)
	else:
	# Now change the directory
		os.chdir( path )
		r=os.getcwd()
	# Check current working directory.
		print r
		hf.write(r)
	hf.close()





