import os
import csv

# file name with extension
fileNames = os.listdir('JP_Custom/input')
# file name without extension
print(len(fileNames))
f = open("JP_Custom/file_log.txt", "a")

for fileName in fileNames:
    tmp = fileName.split('_')
    data = [fileName,tmp[0]]
    # write the data
    f.writelines(fileName+' '+tmp[0]+'\n')
f.close()