import os

def mkdir(arg):
    if(len(arg)>=2):
        path=arg[1]    
        if os.path.exists(path):
            print("Directory already exists!!")
        else:
		os.mkdir(path,0755)
		print("success!!")
    else:
         print("mkdir: missing operand")



