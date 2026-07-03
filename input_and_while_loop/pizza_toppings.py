# Pizza Toppings: Write a loop that prompts the user to enter a series of
# pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.

prompt = '\nEnter your favorite toppins'
prompt += "\nEnter 'quit' to stop asking for toppings "

while True:
    message0 = "What toppings would you like?"
    toppings = input(prompt)
    if toppings == 'quit':
        break
    else:
        print("You'll add " + toppings.title() + " toppings to your pizza")