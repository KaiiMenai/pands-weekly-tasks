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
def count_letter_e_in_file(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            content = file.read() # Read the content of the file.
            # Count occurrences of 'e' (lowercase) and 'E' (uppercase)
            lowercase_e_count = content.count('e')
            uppercase_e_count = content.count('E')
            # Calculate the total count
            total_count = lowercase_e_count + uppercase_e_count
            return lowercase_e_count, uppercase_e_count, total_count
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")
        return 0, 0, 0

# Step 3: Use the function to count and print results
lowercase_count, uppercase_count, total_count = count_letter_e_in_file(filename)

if total_count > 0:
    print(f"The letter 'e' appears {lowercase_count} times as lowercase and {uppercase_count} times as uppercase.")
    print(f"Total occurrences of the letter 'e' (both uppercase and lowercase): {total_count}.")
else:
    print("Failed to count the occurrences of 'e'.")
    
# Output 
# File downloaded and saved as mobydick.txt in pands-weekly-tasks directory.
# The letter 'e' appears 58820 times as lowercase and 826 times as uppercase.
# Total occurrences of the letter 'e' (both uppercase and lowercase): 59646.


# References:
# https://docs.python.org/3/library/urllib.request.html
# https://docs.python.org/3/library/exceptions.html
# https://docs.python.org/3/tutorial/errors.html
    # accounts.py https://github.com/KaiiMenai/pands-weekly-tasks/blob/main/accounts.py
    # collatz.py https://github.com/KaiiMenai/pands-weekly-tasks/blob/main/collatz.py as examples of how to structure the code. As well as examples of using a custom designed function as well as using the if, while, else statements.
# Killbourne and Williams, 2003. https://pmc.ncbi.nlm.nih.gov/articles/PMC1480066/
# https://gist.githubusercontent.com/StevenClontz/4445774/raw/1722a289b665d940495645a5eaaad4da8e3ad4c7/mobydick.txt
# https://gist.github.com/StevenClontz/4445774#file-mobydick-txt
# https://docs.python.org/3/library/urllib.request.html
# https://python.readthedocs.io/fr/stable/howto/urllib2.html
# Discussion on urllib.request.urlretrieve vs urlopen on Stack Overflow - https://stackoverflow.com/questions/56915019/should-i-switch-from-urllib-request-urlretrieve-to-urllib-request-urlopen
# https://www.scivision.dev/python-switch-urlretrieve-requests-timeout/
# File reading with encoding in Python (open() function) - https://melaniewalsh.github.io/Intro-Cultural-Analytics/02-Python/07-Files-Character-Encoding.html
# Counting characters in a string with str.count() method - https://note.nkmk.me/en/python-str-count/
# https://www.programiz.com/python-programming/exception-handling
# https://www.w3schools.com/python/python_try_except.asp
# https://stackoverflow.com/questions/1155617/count-the-number-of-occurrences-of-a-character-in-a-string

# END