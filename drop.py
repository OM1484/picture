import dropbox
class transfer:
    def __init__(self, accesstoken):
        self.accesstoken=accesstoken
    def upload(self, filefrom, fileto):
        dbx=dropbox.Dropbox(self.accesstoken)
        f=open(filefrom, "rb")
        dbx.files_upload(f.read(), fileto)

data=transfer("WC_LQipMFlwAAAAAAAAAAZREShrz06AmYeSlBXhIApkiY0Uw7v73VILBIDEzqcfc")
filefrom=input("Enter the source file ")
fileto=input("destination path ")
data.upload(filefrom, fileto)
print("Files uploaded")