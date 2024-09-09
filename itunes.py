import json
import requests
import sys
#Put this as own file thing for python
#check out old work from python class what i turned in and the code
#Let set a goal for myself here loook for the info ask three questions
#In order for this to run do python itunes.py [artist name]
"""Give me three song recs for hozier(or whatever artist they choose)?, The genre?,or track number """

#Asks how many songs wanted
number = input("Choose song limit: ")
print("For the following questions answer y or n")

if len(sys.argv) != 2:
    sys.exit()


response = requests.get("http://itunes.apple.com/search?entity=song&limit=" + number + "&term="+ sys.argv[1])
#gets printed nicer with json.dumps
#print(json.dumps(response.json(), indent=2))

o = response.json()

question = input("Would you like it if I gave " + number + " song recs: ")
if(question == 'y' or question == 'Y'):
    for result in o["results"]:
            print(result["trackName"])
else:
     print("Ok next question!")

question2 = input("Would you like to know genre of each song? ")
if(question2 == 'y' or question2 == 'Y'):
    for result in o["results"]:
        print(result["primaryGenreName"])
else:
     print("Ok next question!")

question3 = input("Track Number for each song? ")
if(question3 == 'y' or question3 == 'Y'):
     for result in o["results"]:
          print(result["trackNumber"])

print("Thats all the questions!")