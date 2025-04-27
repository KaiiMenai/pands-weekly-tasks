# numberofes_txt.py
# Week 7 task
# This program will read in a text file and print out the number of e's contained therin.
# author: Kyra Menai Hamilton

# Import urllib.request - same as in the es from url. But now will save the url to a text file (locally - i.e. into the repository).
import urllib.request
from urllib.request import urlretrieve

url = "https://gist.githubusercontent.com/StevenClontz/4445774/raw/1722a289b665d940495645a5eaaad4da8e3ad4c7/mobydick.txt"
filename = "mobydick.txt"

urlretrieve(url, filename)
print("File downloaded and saved as mobydick.txt in pands-weekly-tasks directory.")