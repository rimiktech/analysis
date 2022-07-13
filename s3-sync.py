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


from urllib.parse import urlparse

class S3Url(object):

    def __init__(self, url):
        self._parsed = urlparse(url, allow_fragments=False)

    @property
    def bucket(self):
        if '.s3.amazonaws.com' in self._parsed.netloc: return self._parsed.netloc.split('.s3.amazonaws.com')[0]
        return self._parsed.netloc

    @property
    def key(self):
        if self._parsed.query:
            return self._parsed.path.lstrip('/') + '?' + self._parsed.query
        else:
            return self._parsed.path.lstrip('/')

    @property
    def url(self):
        return self._parsed.geturl()






def upload_image(local_file_path, s3_url):
    try:
        if os.path.exists(local_file_path):
            print("Uploading file '{0}'".format(local_file_path))
            
            s = S3Url(s3_url)
            filename = local_file_path.split(s.key.rstrip('/'), 1)[-1].lstrip('\\').replace(os.sep, '/')
            s3_file_path = os.path.join(s.key, filename)
            
            s3_file_exists = lambda s3_file_path: bool(s3.list_objects_v2(Bucket=s.bucket, Prefix=s3_file_path)['KeyCount']) 
            if s3_file_exists(s3_file_path):  
                print("File already exist. Replacing file...")
                s3.upload_file(local_file_path, s.bucket, s3_file_path) # 'upload_file' method would automatically replace file.
                print("Replaced Successfully.")
                return
            
            s3.upload_file(local_file_path, s.bucket, s3_file_path) 
            print("Uploaded Successfully.")      
    except Exception as err:
        print(err)