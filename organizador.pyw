import shutil
import os
import re


os.chdir("C:/Users/Linux/Downloads/")
#print(os.getcwd())
#print(os.listdir("."))
while True:

    for x in os.listdir():
        print(x)
        if(re.search('\\b.zip\\b', x, re.IGNORECASE) or re.search('\\b.rar\\b', x, re.IGNORECASE)):
            print(x)
            shutil.move(x,"C:/Users/Linux/Downloads/zips")
        if (re.search('\\b.torrent\\b', x, re.IGNORECASE)):
            print(x)
            shutil.move(x, "C:/Users/Linux/Downloads/torrents")
        if (re.search('\\b.exe\\b', x, re.IGNORECASE)):
            print(x)
            shutil.move(x, "C:/Users/Linux/Downloads/instaladores-exes")



