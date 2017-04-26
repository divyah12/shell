#!/usr/lib/python
def x(num):
           hf=open("historyfile.py","r")
           aux =open("tempxhistory.txt","w")
           lines=hf.readlines()
           count=0
           for l in lines:
              count=count+1
              if(int(num)==count):
                   print (l)
                   aux.write(l)


