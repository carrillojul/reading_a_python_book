# No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure
# the sandwich 'pastrami' appears in the list at least three times. Add code
# near the beginning of your program to print a message saying the deli has
# run out of pastrami, and then use a while loop to remove all occurrences of
# 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up
# in finished_sandwiches.

sandwiches_orders = ['tuna sandwich', 'pineapple sandwich', 'cheese sandwich', 'pastrami', 'pastrami', 'pastrami']
sandwiches_finished = []

while sandwiches_orders:

    if 'pastrami' in sandwiches_orders:
        del_sandwich = 'pastrami'
        sandwiches_orders.remove(del_sandwich)
    else:
        current_sandwich = sandwiches_orders.pop()
        print("Your " + current_sandwich + "was made!")
        sandwiches_finished.append(current_sandwich)

print('\nthe following sandwiche was made...')
for sandwich in sandwiches_finished:
    print(sandwich.title())