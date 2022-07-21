import glob
import os

my_files = glob.glob('*.txt')
print(my_files)

string1 = 'coding'

# setting flag and index to 0
flag = 0
index = 0

file1 = open("geeks.txt", "r")
for line in file1:  
    index += 1 
    if string1 in line:
      flag = 1
      break 
          
if flag == 0: 
   print('String', string1 , 'Not Found') 
else: 
   print('String', string1, 'Found In Line', index)
  
# closing text file    
file1.close() 