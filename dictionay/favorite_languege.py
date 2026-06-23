favorite_languages = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'julio' : 'python'
}

print("sarah's favorite languages is " + 
      favorite_languages['sarah'].title() + ".\n")


# #adding for loop to loop key-value in the dictionary
# for name, language in favorite_languages.items():
#     print(name.title() + "'s favorite language is "
#           + language.title() + ".\n")

#adding for loop only to the key

frineds = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(name.title())

    if name in frineds:
        print(" Hi " + name.title() + 
              ", I see your favorite language is " + 
              favorite_languages[name].title() + "!")

#here this example shows that method key() is not for "foor loop"
if 'erin' not in favorite_languages.keys():
    print('Erin, please take our poll!s')

#we're gonna order alphabetically 

for name in  sorted(favorite_languages.keys()):
    print(name.title() + ", thank you for taking the poll!")

#we'll print all values by for loop
print('The following language have been mentioned: ')
for lenguage in favorite_languages.values():
    print(lenguage)

#turn the dictionary into a set to not get repetitive values
print('-------------------------------------')
for lenguage in set(favorite_languages.values()):
    print(lenguage.title())