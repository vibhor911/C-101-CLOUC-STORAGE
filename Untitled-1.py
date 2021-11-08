
import os
import dropbox   
from dropbox.files import WriteMode

class TransferData:
    def __init__(self,access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        # enumerate local files respectively
    for root,dirs,files in os.walk(file_from):

        for filename in files:
                # construct the full local path
            local_path = os.path.join(root,filename)

                # construct the full dropbox path
            relative_path = os.path.realpath(local_path,file_from)
            dropbox_path = os.path.join(file_to,relative_path)
                # upload the files
            with open(local_path,'rb') as f:
                dbx.files_upload(f.read(),dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = '1VswB3bQvnIAAAAAAAAAAdhkN2JqFcnS8VxBnL1iQhUnqlv2IBlrTy6llA2kbZUg'
    transferData = TransferData(access_token)

    file_from = str(input("Enter the folder path to transfer : -"))
    file_to = input("Enter the full path to upload to dropbox : -")  
    # This is the full path to upload the files to, including name that you wish the file to be called once uploaded.


    #API v2
    transferData.upload_file(file_from,file_to)
    print("File has been moved !!")

main()