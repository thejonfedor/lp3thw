import json, datetime

with open('userBase.json', 'r') as output:
    read = output.read()
    users = json.loads(read)
    keys = users.keys()

print(f"\nUsers is object type: {type(users)}")

print(f"\nUsers dict has these keys: {keys}")

print(f"\nUsers looks like this: {users}")