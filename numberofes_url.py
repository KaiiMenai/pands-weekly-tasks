# numberofes_url.py
# Week 7 task
# This program will read in a text file and print out the number of e's contained therin.
# author: Kyra Menai Hamilton

# Import modules needed for the functionality of the program.
# Initially I tried to use requests  through "import requests" but it kept telling me that the module was not found. I then tried to install it using pip but it still did not work.
# I did the same with the pandas module and it also didn't work. I am not sure why requests did not work. 
# I then tried to use urllib.request and it worked as expected.
# I chose to use urllib.request as it was the only one that worked for me.
# I assumed with the use of this code that the text file would be in the same directory as the code. I also assumed that the text file would be in the same format as the one provided in the URL.
# An assumption was made that the letter 'e' would be in the text file and that it would be in the correct format for the code to work.
# I assumed that all 'e' letters would be counted and that if there were any other letters in the text file that they would not be counted.
# I assumed that the code would not read special characters or numbers and that it would only read letters.

# Import urllib.request
import urllib.request

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

url = "https://gist.githubusercontent.com/StevenClontz/4445774/raw/1722a289b665d940495645a5eaaad4da8e3ad4c7/mobydick.txt" # URL of the text file

# Use the function to get the counts.
lowercase_count, uppercase_count, total_count = count_letter_e_in_url(url)

# Print the results - I wanted to make sure that I checked both the lowercase and uppercase 'e' characters.
if total_count > 0:
    print(f"The letter 'e' appears {lowercase_count} times as lowercase and {uppercase_count} times as uppercase.")
    print(f"Total occurrences of the letter 'e' (both uppercase and lowercase): {total_count}.")
else:
    print("Failed to count the occurrences of 'e'.")
    
# Output: - When using https://gist.githubusercontent.com/StevenClontz/4445774/raw/1722a289b665d940495645a5eaaad4da8e3ad4c7/mobydick.txt
            # The letter 'e' appears 58820 times as lowercase and 826 times as uppercase.
            # Total occurrences of the letter 'e' (both uppercase and lowercase): 59646.
            # # - When using https://gist.github.com/StevenClontz/4445774#file-mobydick-txt
            # The letter 'e' appears 234844 times as lowercase and 854 times as uppercase.
            # Total occurrences of the letter 'e' (both uppercase and lowercase): 235698.
# I have tested this code with the URL provided and it works as expected. I have also tested it with other URLs and it works as expected.
# I have also tested it with a URL that does not exist and it returns an error message as expected.

# I chose to use the utf-8 encoding as it is the most common encoding for text files, and it avoids issues with non-ASCII characters.

# References:
# https://docs.python.org/3/library/urllib.request.html
# https://docs.python.org/3/library/exceptions.html
# https://docs.python.org/3/tutorial/errors.html
    # accounts.py https://github.com/KaiiMenai/pands-weekly-tasks/blob/main/accounts.py
    # collatz.py https://github.com/KaiiMenai/pands-weekly-tasks/blob/main/collatz.py as examples of how to structure the code. As well as examples of using a custom designed function as well as using the if, while, else statements.
# Killbourne and Williams, 2003. https://pmc.ncbi.nlm.nih.gov/articles/PMC1480066/
# https://gist.githubusercontent.com/StevenClontz/4445774/raw/1722a289b665d940495645a5eaaad4da8e3ad4c7/mobydick.txt
# https://gist.github.com/StevenClontz/4445774#file-mobydick-txt

# END