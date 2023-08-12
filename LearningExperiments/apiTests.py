# IT WORKS!
# CRITICAL learning here: There is urllib3 warning associated with
# script is using an older SSL version and throws a warning when run
# I tried a bunch of ways to catch the warning so it doesn't eff up
# python's requests module. The system python used to run this py
# json response. Turns out the warning is thrown as soon as you
# import the requests module. Moved my warnings import and catch
# statement to the top of the script and viola! Works great now!

import warnings # For ignoring warnings re: urllib3 in MacOS sys python
warnings.filterwarnings("ignore") # Cmd to ignore warnings

import requests, json, datetime, os # Import py modules

# Call API convert to text
response = requests.get("https://randomuser.me/api").text

parsed = json.loads(response) # Load json response as dict

resultsOnly = parsed['results'] # get dict key and values

# visually test output
print(f"THIS IS JUST RESULTS FROM REQUEST:\n{resultsOnly}\n")

resultsDict = resultsOnly[0] # results is a list - need the first item

# visually test output
print(f"resultsDict is type {type(resultsDict)}")

userName = resultsDict['login']['username'] # get username from API results dict

timestamp = datetime.datetime.now() # get current timestamp
strTimestamp = str(timestamp) # convert timestamp to string type

resultsDict.update([('requestedTime',strTimestamp)]) # update results dict with timestamp

# visually test output
print(f"\nHere's the userName dict\n{resultsDict}\n")

newUserDict = {} # create new dict to store enriched results from API (new user)
newUserDict.update([(userName,resultsDict)]) # populate new dict

# visually test output
print(f"\nHere's the new user\n{newUserDict}\n")

isEmpty = os.stat('userBase.json').st_size == 0 # check if userBase.json is empty BOOL

# if statement to handle if file is empty
if isEmpty == True :
    with open('userBase.json', 'w') as output: # open file
        jsonInput = json.dumps(newUserDict, indent = 4) # format json for writing to file
        newUserDictStr = str(jsonInput) # convert to string type
        output.write(newUserDictStr) # write new user from API result to file
else : # else if the file is NOT empty
    with open('userBase.json', 'r') as readMe: # open the userBase file in read mode
        read = readMe.read() # read the existing file into python
        print(f"\nHere's the read variable\n{read}\n") # show contents
        existingUsers = json.loads(read) # load file contents
    with open('userBase.json', 'w') as output: # open the file in write mode
        print(f"existingUsers is type {type(existingUsers)}") # show type
        print(f"existingUsers has these keys {existingUsers.keys()}") # list keys
        print(f"This is the new user's username\n{userName}") # show new username
        print(f"This is the resultsDict\n{resultsDict}") # show dictionary
        existingUsers[userName] = resultsDict # add new user key value pair to dict
        jsonInput = json.dumps(existingUsers, indent = 4) # format json
        output.write(jsonInput) # write updated user list back to file
# list updated keys - all the users
print(f"\nexistingUsers NOW has these keys {existingUsers.keys()}")

print(f"\nexistingUsers is this data type {type(existingUsers)}")

for user in existingUsers:
    print(f"\nHere are the values of the users: {user.values()}")


# How to pretty print JSON in py
# https://stackoverflow.com/questions/12943819/how-to-prettyprint-a-json-file

# jsonFormat = json.dumps(newUserDict, indent = 4)

# with open('userBase.json', 'a') as output:
#     output.write(f"\n{jsonFormat}")

# -------------------------
# This is where I left off
# -------------------------