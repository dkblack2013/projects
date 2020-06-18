import json
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