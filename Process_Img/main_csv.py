import os
import csv

# file name with extension
fileNames = os.listdir('JP_Custom/input')
# file name without extension
print(len(fileNames))
f = open("JP_Custom/file_log.csv", "a")
writer = csv.writer(f)
for file in fileNames:
    tmp = file.split('_')
    data = [file,tmp[0]]
    # write the data
    writer.writerow(data)

    # f.write(file+" "+tmp[0]+"\n")
f.close()