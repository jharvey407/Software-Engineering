# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 03:19:59 2020

@author: James
"""



# Create a nested dictionary of rare birds and their attributes
rarebirds = {
    'Gold-Crested Toucan': {
        'Height (m)': 1.1,
        'Weight (kg)': 35,
        'Color': 'Gold',
        'Endangered': True,
        'Aggresive': True  },

    'Pearlescent Kingfisher': {
        'Height (m)': 0.25,
        'Weight (kg)': 0.5,
        'Color': 'White',
        'Endangered': False,
        'Aggresive': False     },

    'Four-Metre Hummingbird': {
        'Height (m)': 0.6,
        'Weight (kg)': 0.5,
        'Color': 'Blue',
        'Endangered': True,
        'Aggresive': False    },

    'Giant Eagle':{
        'Height (m)': 1.5,
        'Weight (kg)': 52,
        'Color': 'Black and White',
        'Endangered': True,
        'Aggresive': True },

    'Ancient Vulture': {
        'Height (m)': 2.1,
        'Weight (kg)': 70,
        'Color': 'Brown',
        'Endangered': False,
        'Aggresive': False }
}        

# Create a list of bird locations base on our position
birdlocation = ["In the canopy directly above our heads.",
    "Between my 6 and 9 o'clock above.",
    "Between my 9 and 12 o'clock above.",
    "Between my 12 and 3 o'clock above.",
    "Between my 3 and 6 o'clock above.",
    "In a nest on the ground.",
    "Right behind you."
]

# Create a dictionary of location codes and assign locations from the birdlocation list
codes = { '001': birdlocation[0],
    '010': birdlocation[1],
    '011': birdlocation[2],
    '100': birdlocation[3],
    '101': birdlocation[4],
    '110': birdlocation[5],
    '111': birdlocation[6]
}

# Creat a list of actions to use when sighting birds
actions = ['Back Away',
    'Cover our Heads',
    'Take a Photograph'
]

# Print whether the Giant Eagel is dangerous or not
print("Is the Giant Eagle aggresive?:", rarebirds['Giant Eagle']['Aggresive'])
print()

# Print the name of each bird and whether or not it is
# Aggresive or Endangered
print('Our list of rare birds:')
for bird in rarebirds:
    print(bird)
    if rarebirds[bird]['Aggresive']:
        print('Aggresive:', actions[1])
    else:
        print('Aggresive: No')
    if rarebirds[bird]['Endangered']:
        print('Endangered:', actions[0])
    else:
        print('Endangered: No')
    print()

# Print a list of our codes to use as reference
print('Codes:')
for k, v in codes.items():
    print(k, v)
print()

# Update our rarebirds dictionary with key Seen set to False
for k, v in rarebirds.items():
    v['Seen'] = False

# Print command for testing
# print(rarebirds)

# Create a list of rare birds from our dictionary to use as a reference for sighting
rarebirdslist = []
for bird in rarebirds.keys():
    rarebirdslist.append(bird.lower())

# print command for testing
# print(rarebirdslist)

# Create an Encounter variable with the default value of True
encounter = False

while not encounter:
    # Ask the user what bird they have seen
    sighting = input('What did you see? ').lower()

    # Compare our sighting to our rarebirds list, print confirmation message
    if sighting in (rarebirdslist):
        print("This is one of the birds we're looking for!")
        encounter = True
    else:
        print("That's not one of the birds we're looking for.")
    

# Ask the user for the location code for the sighting of the bird
code = input("Where did you see it? Input the correct code:")
location = codes[code]

# Output the bird seen and it's location
print("So you've seen a", sighting.title(), location, "My goodness.")

# If the bird sighted is aggresive, print a warning
if rarebirds[sighting.title()]['Aggresive']:
    print('The', sighting.title(), 'is aggresive.', actions[0], 'and', actions[1],'.')
    print(actions[2], 'of the', sighting.title(), 'at', codes[code].lower())
# If the bird is engangerd, print instructions
elif rarebirds[sighting.title()]['Endangered']:
    print(actions[2], 'of the', sighting.title(), 'at', codes[code].lower())
# If the bird is neither endangered nor aggresive, print instructions    
else:
    print(actions[2], 'of the', sighting.title(), 'at', codes[code].lower())



  

