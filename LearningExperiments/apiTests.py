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

print(f"\nHere's the new user\n{newUserDict}\n")

with open('userBase.json', 'r') as output:
    read = output.read()
    print(f"\nHere's the read variable\n{read}\n")
    existingUsers = json.loads(read)
    print(f"existingUsers is type {type(existingUsers)}")
    print(f"existingUsers has these keys {existingUsers.keys()}")
    print(f"This is the username\n{userName}")
    print(f"This is the resultsDict\n{resultsDict}")
    existingUsers[userName] = resultsDict

print(f"\nHere's the existingUsers dictionary\n{existingUsers}\n")

print(f"existingUsers NOW has these keys {existingUsers.keys()}")


# -------------------------
# This is where I left off
# NOW I need to rewrite the part of this script that
# writes the NEWLY updated dict back to the userBase.json file
# -------------------------

# How to pretty print JSON in py
# https://stackoverflow.com/questions/12943819/how-to-prettyprint-a-json-file

# jsonFormat = json.dumps(newUserDict, indent = 4)

# with open('userBase.json', 'a') as output:
#     output.write(f"\n{jsonFormat}")

'''

name = resultsDict['name']
locationKeys = resultsDict['location'].keys()
locationStreet = resultsDict['location']['street']

print(f"\n{name} \n{locationStreet} \n  ")
# -------------------------
# This is where I left off
# -------------------------

'''