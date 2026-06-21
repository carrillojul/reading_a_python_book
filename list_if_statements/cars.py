cars = ['audi', 'bmw','subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
       print(car.title())


#car = 'audi'
#car == 'bmw' #chequeamos igualdad desde la consola porque por aqui no lo permite
# este caso es falso porqe car tiene el valor de audi
#car == 'audi' este seria el caso verdadero
#car == 'Audi' pero este retorna falso a pesar de ser la
#misma palabra porque es case sensitive, es decir, 
#si tiene una letra en mayuscula para ser igual, tienen
#que tenerlo ambos
#para que lea sin mayuscula la variable a comparar tendremos
#que usar la funcion de lowercase, para eliminarle cualquier
#letra en mayuscula
#ejemplo de como quedaria
#car = 'Julio'
#car.lower() = 'julio'
#True
#si imprimimos car
#resultado seria 'julio' todo en minusculas
