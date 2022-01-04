import os 
import shutil
path=input("Enter your path ")
files=os.listdir(path)
for i in files:
    name, ext=os.path.splitext(i)
    ext=ext[1:]
    if ext=="":
        continue
    if os.path.exists(path+"/"+ext):
        shutil.move(path+"/"+i, path+"/"+ext+"/"+i)
    else:
        os.mkdir(path+"/"+ext)
        shutil.move(path+"/"+i, path+"/"+ext+"/"+i)