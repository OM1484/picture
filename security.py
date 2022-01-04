import dropbox
import time 
import random
start=time.time()

def transfer(name):
    dbx=dropbox.Dropbox("9U72Sl5oikAAAAAAAAAAARaDPNS-F6UOCi9IzqO54TwV0JgoX4l0TB-H8GNzkd_H")
    f=open(name, "rb")
    dbx.files_upload(f.read(), "/"+name)
    print("Files uploaded")
import cv2
def takepicture():
    video=cv2.VideoCapture(0)
    result=True
    num=random.randint(0, 100)
    while(result):
        ret, frame=video.read()
        name="img"+str(num)+".png"
        cv2.imwrite(name, frame)
        result=False 
    print("picture taken")
    video.release()
    cv2.destroyAllWindows()
    return name
def main():
    while True:
        if((time.time()-start)>=5):
            name=takepicture()
            transfer(name)
main()