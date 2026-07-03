responses = {}
polling_active = True
while polling_active:
    #Prompt for the person's name and response
    name = input("\nWhat is your name?")
    response = input("\nWhich moutain would you like to climb someday?")

    #store the response in the dictionary:
    responses[name] = response
    
    #find out if anyone else is going to talk the poll.
    repeat = input("would you like to let other person respond? (yes/ no)")
    if repeat == 'no':
        polling_active = False

#polling is complete. show the results.
print("\n----Poll results-----")
for name, response in responses.items():
    print(name + " would like to climb " + response + ".")