# IT WORKS!
# CRITICAL learning here: There is urllib3 warning associated with
# script is using an older SSL version and throws a warning when run
# I tried a bunch of ways to catch the warning so it doesn't eff up
# python's requests module. The system python used to run this py
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

print(f"\nHere's the userName dict\n{resultsDict}\n")

newUserDict = {}
newUserDict.update([(userName,resultsDict)])

# -------------------------
# This is where I left off
# Here I NEED to try loading in the userBase.json file
# as a dict and updating it as a dict vs trying to update it as a json file
# -------------------------

print(f"\nHere's the new user\n{newUserDict}\n")

# How to pretty print JSON in py
# https://stackoverflow.com/questions/12943819/how-to-prettyprint-a-json-file

jsonFormat = json.dumps(newUserDict, indent = 4)

with open('userBase.json', 'a') as output:
    output.write(f"\n{jsonFormat}")

'''

name = resultsDict['name']
locationKeys = resultsDict['location'].keys()
locationStreet = resultsDict['location']['street']

print(f"\n{name} \n{locationStreet} \n  ")
# -------------------------
# This is where I left off
# -------------------------

'''