pizzas = ['peperoni', 'napolitana', 'hawaiana']
for pizza in pizzas:
    print('I like ', pizza)
print('I really love pizza')


friend_pizzas = pizzas[:]

pizzas.append("bbq")
friend_pizzas.append("vegetable")
print(f"-------------------\nMy favorite pizza are: ")
for pi in pizzas:
    print(pi)
print(f"-------------------\nMy friend's pizzas are: ")
for pi2 in friend_pizzas:
    print(pi2)
