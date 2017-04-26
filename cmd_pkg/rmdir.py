import shutil
import os

def rmdir(arg):
    if(len(arg)>=2):
        path=arg[1]
        if not os.path.exists(path):
		print("No Such Directory!!")
        else:
		shutil.rmtree(path)
		print("success!!")
    else:
        print("rmdir: missing operand")



