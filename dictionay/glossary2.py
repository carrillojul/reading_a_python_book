# Glossary 2: Now that you know how to loop through 
# a dictionary, clean
# up the code from Exercise 6-3 (page 102) by replacing 
# your series of print
# statements with a loop that runs through the dictionary’s
#  keys and values.
# When you’re sure that your loop works, add five more 
# Python terms to your


#the same dictionary used in glassary.py
glossary = {
    'syntaxis' : 'it is the way how we should write statement code like for loop or if-elif-else chain',
    'indentation' : 'it is a whitespace we should leave when we are using for loop or if-elif-else',
    'list' : 'it is a space where we can store serveral value to then use it how we want to',
    'dictionary' : 'it is a callection of key-value. we work with it to store some data of an object',
    'variable' : 'it is a space reserve in the memory to add a value. afterward we can use its value through the variable, calling it'
}

for key, value in glossary.items():
    print(key.title() + ": " + value + "\n")

glossary['set'] = 'inmutable collection of data'
glossary['model'] = 'it is a notation from the abstract world that can implement in programming'
glossary['information'] = 'it is a collection of data, many data'
glossary['algorithm'] = 'it is a secuency of step to reach a solution or a way to find out anything'
glossary['program'] = 'it is a solution to activities that used to be a problem'

print('-----------------------------------------------------')
print('these are the word that learn through the course\n')
for k, v in glossary.items():
    print(k.title() + ': ' + v + ".\n")
    