# Movie Tickets: A movie theater charges different ticket prices depending on
# a person’s age. If a person is under the age of 3, the ticket is free; if they are
# between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
# $15. Write a loop in which you ask users their age, and then tell them the cost
# # of their movie ticket.

prompt = "\nEnter customer age"

while True:
    age = input(prompt)
    if int(age) < 3:
        print('your ticket is free')
        break
    elif int(age) <= 12:
        print('your ticket costs $10')
        break
    else:
        print('your ticket costs $15')
        break