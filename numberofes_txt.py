# numberofes_txt.py
# Week 7 task
# This program will read in a text file and print out the number of e's contained therin.
# author: Kyra Menai Hamilton

# Import urllib.request - same as in the es from url. But now will save the url to a text file (locally - i.e. into the repository).
import urllib.request
from urllib.request import urlretrieve

url = "https://gist.githubusercontent.com/StevenClontz/4445774/raw/1722a289b665d940495645a5eaaad4da8e3ad4c7/mobydick.txt"
filename = "mobydick.txt"

try:
    urlretrieve(url, filename)
    print("File downloaded and saved as mobydick.txt in pands-weekly-tasks directory.")
except Exception as e:
    print(f"Error downloading file: {e}")
    exit(1)
    
# Function to count occurrences of the letter 'e' in a file from a URL.
def count_letter_e_in_url(url):
    try:
        # Open the URL and read the content
        with urllib.request.urlopen(url) as response:
            content = response.read().decode('utf-8')  # Decode the content to a string
            
            # Count occurrences of 'e' (lowercase) and 'E' (uppercase)
            lowercase_e_count = content.count('e')
            uppercase_e_count = content.count('E')
            
            # Calculate the total count
            total_count = lowercase_e_count + uppercase_e_count
            
            return lowercase_e_count, uppercase_e_count, total_count
    except Exception as e:
        print(f"An error occurred: {e}")
        return 0, 0, 0
