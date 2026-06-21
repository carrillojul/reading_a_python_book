car = 'subaru'

if car == 'subaru':
    print('I predict True')
    print(car)

#second example
if car == 'audi':
    print('I predict false')
car = 'audi'
print(car)

print('--------------------------')
name = 'Julio'
if name == 'julio':
    print('Hola, soy Julio')
    #False

if name.lower() == 'julio':
    print('Este si es verdadero')
#True

number = 10
if number == 2:
    print('son similares')
#false

if number > 2:
    print('True')
#True

if number != 2:
    print('number no es 2')
#True

if number != 10:
    print('number si es 10')
#false


