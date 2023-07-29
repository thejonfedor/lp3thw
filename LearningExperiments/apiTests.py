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

# How to pretty print JSON in py
# https://stackoverflow.com/questions/12943819/how-to-prettyprint-a-json-file
# enrichJSON = json.
jsonFormat = json.dumps(parsed, indent = 4)

print(f"\n{parsed} \n")

results = parsed['results']

print(f"\n{results} \n ")

resultsDict = results[0]

timestamp = datetime.datetime.now()
strTimestamp = str(timestamp)

resultsDict.update([('requested',strTimestamp)])

print(f"\n{resultsDict} \n ")

name = resultsDict['name']
locationKeys = resultsDict['location'].keys()
locationStreet = resultsDict['location']['street']
'''
print(f"\n{name} \n{locationStreet} \n  ")
'''


# with open('jsonResponse.json', 'w') as output:
#     output.write(jsonFormat)