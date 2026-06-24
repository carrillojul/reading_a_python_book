# People: Start with the program you wrote for Exercise 6-1 (page 102).
# Make two new dictionaries representing different people, and store all three
# dictionaries in a list called people. Loop through your list of people. As you
# loop through the list, print everything you know about each person.

person_0 = {
            'first' : 'julio',
            'last' : 'carrillo',
            'age' : 27,
            'city' : 'medellin'}
        
person_1 = {
            'first' : 'cesar',
            'last' : 'corre',
            'age' : 25,
            'city' : 'itagui'}

person_2 = {
            'first' : 'valentina',
            'last' : 'jaramillo',
            'age' : 25,
            'city' : 'envigado'}

people = []


for i in range(3):
    if i == 0:
        people.append(person_0)
    elif i == 1:
        people.append(person_1)
    else:
        people.append(person_2)

for person in people:
    if person['first'] == 'julio':
        print('this is: ' + person['first'] + " "+
              person['last'] + ', his age is: ' + 
              str(person['age']) + ', he is from ' + person['city'] + "\n")
    elif person['first']  == 'cesar':
        print('this is: ' + person['first'] + " "+
        person['last'] + ', his age is: ' + 
        str(person['age']) + ', he is from ' + person['city'] + "\n")
    else:
        print('this is: ' + person['first'] + " "+
        person['last'] + ', his age is: ' + 
        str(person['age']) + ', he is from ' + person['city'] +"\n")


