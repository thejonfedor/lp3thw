# IT WORKS!
# CRITICAL learning here: There is urllib3 warning associated with
# python's requests module. The system python used to run this py
# script is using an older SSL version and throws a warning when run
# I tried a bunch of ways to catch the warning so it doesn't eff up
# json response. Turns out the warning is thrown as soon as you
# import the requests module. Moved my warnings import and catch
# statement to the top of the script and viola! Works great now!

import warnings
warnings.filterwarnings("ignore")

import requests, json, datetime

response = requests.get("https://randomuser.me/api").text

parsed = json.loads(response)

resultsOnly = parsed['results']

print(f"THIS IS JUST RESULTS FROM REQUEST:\n{resultsOnly}\n")

resultsDict = resultsOnly[0]

print(f"resultsDict is type {type(resultsDict)}")

userName = resultsDict['login']['username']

timestamp = datetime.datetime.now()
strTimestamp = str(timestamp)

resultsDict.update([('requestedTime',strTimestamp)])

newUserDict = {}
newUserDict.update([(userName,resultsDict)])

print(f"\nHere's the new user\n{newUserDict}\n")

with open('userBase.json','r') as oldFile:
    strOldFile = str(oldFile)
    readOldFile = json.loads(strOldFile)

# -------------------------
# This is where I left off
# -------------------------

print(f"\nreadOldFile is type {type(readOldFile)}\n")

print(f"\nHere's the loaded file {readOldFile}\n")

# How to pretty print JSON in py
# https://stackoverflow.com/questions/12943819/how-to-prettyprint-a-json-file

jsonFormat = json.dumps(newUserDict, indent = 4)

with open('jsonResponse.json', 'w') as output:
    output.write(f"\n{jsonFormat}")

'''
print(f"\nThis is PARSED\n{parsed} \n")

print(f"\nTHIS IS ONLY 'RESULTS'\n{results} \n ")

print(f"\nTHIS IS AN UPDATED 'RESULTS'\n{resultsDict} \n ")

name = resultsDict['name']
locationKeys = resultsDict['location'].keys()
locationStreet = resultsDict['location']['street']

print(f"\n{name} \n{locationStreet} \n  ")
'''