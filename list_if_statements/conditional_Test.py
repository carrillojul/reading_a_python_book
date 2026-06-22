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

boolean = True

if boolean != False:
    print('El boolean es True')
#True

if boolean == False:
    print('boolean es True')

#False

color = 'blue'

if color.title() == 'Blue':
    print('coinciden por la funcion title()')
#True

if color != 'Blue':
    print('Es verdadero porque no son iguales')
#True

if color.title == 'Amarillo':
    print('No pasa nada')
#False

name_uppercase = 'JULIO'

if name_uppercase.lower() == 'julio':
    print('Si porque usamos la function lower()')

if name_uppercase != 'julio':
    print('es verdadero poruqe no son iguales')

numerical_number = 100

if numerical_number == 2:
    print('Esto es falso')

if numerical_number > 101:
    print('False porque numerical_number es 100')

if numerical_number < 101:
    print('Verdadero su valor es: ', numerical_number)

if  numerical_number >= 99:
    print("It's true, numerical_number is:", numerical_number)

if numerical_number <= 99:
    print("no, it is:",numerical_number)

if numerical_number != 99:
    print('numerical number is', numerical_number)

if (numerical_number >= 100) and (numerical_number <= 101):
    print('hi')

if (numerical_number != 100) or (numerical_number > 2):
    print('It is', numerical_number)


if (numerical_number != 100) or (numerical_number > 101):
    print(numerical_number, 'it does not pass')

number_list = [1,2,3,4,5,6,7,8,9]
number_1 = 2
number_2 = 10

if number_1 in number_list:
    print('It is there')

if number_2 not in number_list:
    print('the message will print it because number_2 is not in the list')
    #But if we try with number_1, the message wont be printed

