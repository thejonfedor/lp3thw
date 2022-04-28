# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

# print some states
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

# do it by using the state then cities dict
print('-' * 10)
print("Michigan has: ",cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

# print every state abbreviation
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

# print every city in state
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

# now do both at the same time
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-' * 10)
# safely get an abbreviation by state that might not be there
state = states.get('Texas')

if not state:
    print("Sorry, no Texas.")

# get a city with a default value
city = cities.get('TX', 'Does Not Exist')
print(f"The city for the state 'TX' is: {city}")

print(f"\n", cities)

print(f"\n", states)

# plain old list of keys in dict, states
print(f"\n", list(states.items()))

print(' '.join(cities))

# get individual keys and values in a comma-separated list
print("--These are keys:", ', '.join(cities.keys()), "\n--These are values:", ', '.join(cities.values()))

'''
Exercise Notes for ex39: Dictionaries, Oh Lovely Dictionaries
1. Dicts are pretty cool. Looks a lot like JSON.
   I looked it up and JSON *looks* similar to dict data type
   But dict is a data STRUCTURE deeply embedded in Python vs
   JSON is just a way to represent / store data in a text file
2. OrderedDict objects look pretty cool. Need to do some practice working
   with them and implementing them
   https://docs.python.org/3/library/collections.html#ordereddict-objects 
'''