# The first task below is to make a dictionary called rarebirds whose keys are the names of the birds above, and whose values are themselves dictionaries with the keys: Height (m), Weight (kg), Colour, Endangered, Aggressive. We'll get you started on how this would look, and you can complete it:
rarebirds = {
    'Gold-crested Toucan': {
        'Height (m)': 1.1,
        'Weight (kg)': 35,
        'Color': 'Gold',
        'Endangered': True,
        'Aggressive': True
    },
    'Pearlescent Kingfisher': {
        'Height (m)': .25,
        'Weight (kg)': .5,
        'Color': 'White',
        'Endangered': False,
        'Aggressive': False
    },
    'Four-metre Hummingbird': {
        'Height (m)': 0.6,
        'Weight (kg)': 0.5,
        'Color': 'Blue',
        'Endangered': True,
        'Aggressive': False
    },
    'Giant Eagle': {
        'Height (m)': 1.5,
        'Weight (kg)': 52,
        'Color': 'Black and White',
        'Endangered': True,
        'Aggressive': True
    },
    'Ancient Vulture': {
        'Height (m)': 2.1,
        'Weight (kg)': 70,
        'Color': 'Brown',
        'Endangered': False,
        'Aggressive': False
    }
}
# If you spot a bird, you need a very simple way of telling your photographer where it is.
# Make a list called birdlocation with the following 7 elements (made into strings)
​
birdlocation = [
    "In the canopy directly above our heads.",
    "Between my 6 and 9 o’clock above.",
    "Between my 12 and 3 o’clock above.",
    "Between my 3 and 6 o’clock above.",
    "In a nest on the ground.",
    "Right behind you."
]
​
# Write a dictionary called codes whose keys are the binary codes (of length 3) - written either ‘HHH’ or ‘111’, depending on the system you’ve chosen - and whose values are the members of birdlocation. If this isn't making sense, check out the binary resource we've prepared for you.
codes = {
    "111",
    "110",
    "101",
    "100",
    "011",
    "010",
    "001",
    "000"
}
​
# Make a list called actions, containing the following strings: 'Back Away’, 'Cover our Heads','‘Take a Photograph'.
actions = [ 'Back Away', 'Cover our Heads', 'Take a Photograph' ]
​
# Your photographer has heard that the Giant Eagle has killed adult gorillas before. She wants to know if it's aggressive.
# Using your rarebirds dictionary, print out the Giant Eagle’s value for the ‘aggressive’ key within the nested dictionary (hint: you should be printing out the Boolean True).
​
print(rarebirds["Giant Eagle"]['Aggressive'])
​
for r_birds in rarebirds:
    print("names: ", r_birds)
    if rarebirds[r_birds]['Aggressive'] == True:
        print(actions[1])
    if rarebirds[r_birds]['Endangered'] == True:
        print(actions[0])
​
# Using a for loop, iterate through the keys and the values of the codes dictionary.
for c in codes:
    print(c)
​
# Using a for loop, add an extra bird attribute (to go with with height, weight, etc) called 'seen', and set its value to False for all birds.
​
for birds_seen in rarebirds:
    # print(rarebirds[birds_seen])
    rarebirds[birds_seen].update( {'Seen' : False} )
​
encounter = True
​
# Ask the user for an input, and give them the prompt: ‘What do you see?’. Store this input in a variable called sighting.
# Make this input all lowercase with a built-in function.
sighting = input("What do you see? ").lower()
print(sighting)