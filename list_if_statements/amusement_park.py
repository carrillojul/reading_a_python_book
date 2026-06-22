age = 66

if age < 4:
    print('your admission cost is $0')
    price = 0
elif age < 18:
    price = 7
elif age < 65:
    price = 10
elif age >=65:
    price = 5

print('Your admission cost is $' + str(price) + ".")