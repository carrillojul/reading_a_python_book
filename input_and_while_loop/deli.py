# Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches. Loop
# through the list of sandwich orders and print a message for each order, such
# as I made your tuna sandwich. As each sandwich is made, move it to the list
# of finished sandwiches. After all the sandwiches have been made, print a
# message listing each sandwich that was made.

sandwiches_orders = ['tuna sandwich', 'pineapple sandwich', 'cheese sandwich']
sandwiches_finished = []

while sandwiches_orders:
    current_sandwich = sandwiches_orders.pop()
    print('I made your ' + current_sandwich)

    sandwiches_finished.append(current_sandwich)

print('\nthe following sandwiche was made...')
for sandwich in sandwiches_finished:
    print(sandwich.title())