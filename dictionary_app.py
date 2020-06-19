import json
import difflib
data = json.load(open('original.json'))

go = 'x'
while go != 'y':
    print('\nSearch the dictionary by typing your word and hitting enter.')
    search = input()
    search = search.lower()
    print(data[search])
    print('\nPress y to quit.\nPress anything else to look up another word.')
    go = input()
print("Thank you for using our dictionary!")

#print(difflib.get_close_matches(search, data, cutoff=1))

import json
from difflib import get_close_matches

data = json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word , data.keys())) > 0 :
        print("did you mean %s instead" %get_close_matches(word, data.keys())[0])
        decide = input("press y for yes or n for no")
        if decide == "y":
            return data[get_close_matches(word , data.keys())[0]]
        elif decide == "n":
            return("pugger your paw steps on wrong keys ")
        else:
            return("You have entered wrong input please enter just y or n")
    else:
        print("pugger your paw steps on wrong keys")



word = input("Enter the word you want to search")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)
