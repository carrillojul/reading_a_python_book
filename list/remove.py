#eliminando elemento por su valor
motorcycles = ['honda', 'yamaha', 'suzuki', 'ducati'] 

motorcycles.remove('honda')
print(motorcycles)

motorcycles1 = ['honda', 'yamaha', 'suzuki', 'ducati']
print(motorcycles1)

too_expensive = 'ducati'
motorcycles1.remove(too_expensive)
print(motorcycles1)
print("\nA " + too_expensive.title() + " is too expensive for me.")