import sys
import csv
from typing import List, Any
import os
import wget

path = os.getcwd()

try:
    filename = sys.argv[1]

except:
    print(
        '\nERROR: Please enter the .csv file to download\nUse:$ spring-download.py Springer Direct Links.csv\n')
    sys.exit(0)

def createFolder(folder):
    try:
        os.mkdir(folder)
    except OSError:
        return

with open(filename, 'r') as csvfile:
    csv_reader = csv.reader(csvfile)
    filesDowloaded = 0
    filesNotDownloaded: List[Any] = []

    print('Downloading files...')

    for row_index, row in enumerate(csv_reader):
        if row[0] == "1":
            try:
                createFolder(row[2])
                wget.download(row[4], out=path+'/' + row[2] + '/' + row[1] + ".pdf")
                print('/' + row[2] + '/' + row[1] + ".pdf")
                filesDowloaded = filesDowloaded + 1
            except:
                filesNotDownloaded.append(row[1])

    print(filesDowloaded, ' file(s) downloaded!')
    if filesNotDownloaded != []: print('ERROR: Not downloaded files:\n', filesNotDownloaded)