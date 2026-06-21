motorcycles = ['yamaha', 'honda', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati' #aqui podemos cambiar elemento por index
print(motorcycles)

motorcycles.append('bmw')
print(motorcycles)

motorcycles1 = []
motorcycles1.append('yamaha')

motorcycles1.append('honda')

motorcycles1.append('suzuki')
print(motorcycles1)
motorcycles1.insert(0, 'ducati')
print(motorcycles1)

del motorcycles1[1]
print(motorcycles1)

