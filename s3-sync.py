'''
Task 1: Create a program which will sync all local files to s3 bucket from a folder

Task 2: 
'''
import os
import pdb
import boto3


ACCESS_KEY = "xxxx"
SECRET_KEY = "xxxx"
BUCKET_NAME = "xxxx"
source_path = "D:\\Data Files\\"

s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY, aws_secret_access_key=SECRET_KEY)

def on_file_read(filepath):
    try:
        if os.path.exists(filepath):
            print("Uploading file '{0}'".format(filepath))
            s3_file_path = filepath.split(source_path)[1]

            s3_file_path = s3_file_path.replace(os.sep, '/')

            s3.upload_file(filepath, BUCKET_NAME, s3_file_path)

            print("Uploaded Successfully")      
    except Exception as err:
        print(err)
    
if __name__ == "__main__":
    on_file_read()