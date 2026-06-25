#  Pets: Make several dictionaries, where the name of each dictionary is the
# name of a pet. In each dictionary, include the kind of animal and the owner’s
# name. Store these dictionaries in a list called pets. Next, loop through your list
# and as you do print everything you know about each pet.
pet_0 = {
    'name' : 'poncho',
    'color' : 'brown',
    'animal' : 'dog',
    'owner' : 'valentina'
}

pet_1 = {
    'name' : 'cronox',
    'color' : 'cream',
    'animal' : 'bulldog frances',
    'owner' : 'la tuya'
}

pet_2 = {
    'name' : 'loki',
    'color' : 'grey',
    'animal' : 'dragon',
    'owner' : 'julio'
}

pets = []

for i in range (3):
    if i == 0:
        pets.append(pet_0)
    elif i == 1:
        pets.append(pet_1)
    else:
        pets.append(pet_2)

for pet in pets:
    if pet['name'] == 'loki':
        print(pet['name'].title() + ' is a ' + pet['animal']
              + ' its owner is ' + pet['owner'].title() + ' is a' + 
              pet['animal'] + '. its color is ' + pet['color']
              + ' it is so beautiful\n')
    elif pet['name'] == 'cronox':
        print(pet['name'].title() + ' is a ' + pet['animal']
              + ' its owner is ' + pet['owner'].title() + ' is a' + 
              pet['animal'] + '. its color is ' + pet['color']
              + ' it is so beautiful\n')
    else:
        print(pet['name'].title() + ' is a ' + pet['animal']
              + ' its owner is ' + pet['owner'].title() + ' is a' + 
              pet['animal'] + '. its color is ' + pet['color']
              + ' it is so beautiful\n')