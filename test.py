'''
Filename format: "_<sub-folder>#_<sub-folder> <date>....bmp" like "_ES#_5 220709 13.55.47 098.3A1.bmp"

We have a function which will create new file path based on file name.
function will return new path based on file name like "destpath/sub-folder/sub-folder/date/filename.bmp"

Please modify this function to create destination path and copy the file.
'''

import os
import shutil

def copy(filepath, destpath):
    try:
        if not os.path.exists(filepath): 
           print("{} doesn't exists.".format(filepath))
           return None

        filename = os.path.basename(filepath)
        segments = filename.split("_")
        if len(segments) < 3:
            print("{} is invalid.".format(filename))
            return None

        subfolder1, segments = segments[1].replace("#", ""), segments[2].split()
        if len(segments) < 3:
            print("{} is invalid.".format(filename))
            return None

        subfolder2, date, filename = segments[0], segments[1],  "".join(segments[2:])
        destpath = "{0}\\{1}\\{2}\\{3}\\{4}".format(destpath, subfolder1, subfolder2, date, filename)

        path = os.path.dirname(destpath)
        if not os.path.exists(path):
            os.makedirs(path, exist_ok=True)
        
        shutil.copyfile(filepath, destpath)
        return destpath
    except Exception as ex:   
        print(ex)
        return None


result = copy("D:\\Projects\\OpenAI\\data\\_ES#_5 220709 13.55.47 098.3A1.png", "")
print(result)