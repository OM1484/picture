import os 
#print(os.system("date")) gives current date
#print(os.system("time")) gives current time

#os.mkdir("/Users/91841/OneDrive/Desktop/module") create folder
#print(os.getcwd()) get your current location
#print(os.path.exists("/Users/91841/OneDrive/Desktop/mouse")) check the path existing or not
#x=os.path.splitext("/Users/91841/OneDrive/Desktop/py/hello.txt")  split path and extension
#print(x)
#print(x[0])
#print(x[1])
#print(os.listdir()) to print the list of files and folder
import shutil
source=input("Enter the source folder ")
des=input("Enter your destination folder ")
source=source+"/"
des=des+"/"
files=os.listdir(source)
for i in files:
    shutil.copy((source+i),des)