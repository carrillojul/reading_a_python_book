requested_toppings = ['mushroom', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print('sorry, we are out of green peppers')
    else:
        print('adding ' + requested_topping + ".")
print('\nfinished making your pizza')

print('-----------------------------------------------')

#other exercise where the list starts empty
requested_toppings1 = []
if requested_toppings1:
    for requested_topping1 in requested_toppings1:
        print('adding ' + requested_topping1 + '.')
    print('\nFinished making your pizza!')
else:
    print('are you sure you want a plain pizza?')

print('-----------------------------------------------')


available_toppings = ['mushroom', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']

requested_toppings2 = ['mushroom', 'french fries', 'extra cheese']

for requested_topping2 in requested_toppings2:
    if requested_topping2 in available_toppings:
        print('adding ' + requested_topping2)
    else:
        print('Sorry, we dont have ' + requested_topping2 + '.')
print('\nFinished making your pizza')