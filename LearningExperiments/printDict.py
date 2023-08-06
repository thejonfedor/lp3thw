import json, datetime

with open('userBase.json', 'r') as output:
    read = output.read()
    users = json.loads(read)
    keys = users.keys()

print(f"Users is object type: {type(users)}")

print(f"Users dict has these keys: {keys}")