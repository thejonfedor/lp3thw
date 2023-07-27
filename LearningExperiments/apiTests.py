import requests
import json

response = requests.get("https://randomuser.me/api/")
# print(response.text)

responseDetail = response.text

parsed = json.loads(responseDetail)

# How to pretty print JSON in py
# https://stackoverflow.com/questions/12943819/how-to-prettyprint-a-json-file
jsonFormat = json.dumps(parsed, indent = 4)

print(jsonFormat)

with open('jsonResponse.json', 'w') as output:
    output.write(jsonFormat)