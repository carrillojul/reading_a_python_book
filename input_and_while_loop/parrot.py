
prompt = "\nEnter quit to end the program: "
#print(prompt) para seguir el ejercio tuve que momentar esta linea


#adding a wihle lopp like the example in the book
#message = ""
#we add flags

active = True

while active:
    message = input(prompt)
    
    if message == 'quit':
        active = False
    else:
        print(message)
