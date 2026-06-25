#  Extensions: We’re now working with examples that 
# are complex enough
# that they can be extended in any number of ways. 
# Use one of the example programs from this chapter, 
# and extend it by adding new keys and values, changing 
# the context of the program or improving the formatting 
# of the output.

person = {
    'first_name' : 'julio',
    'last_name' : 'carrillo',
    'age' : 27,
    'city' : 'medellin'
}

person['country'] = 'Colombian'

if 'tall' not in person.items():
    person['tall'] = str(190) + "cm"
    print(person)