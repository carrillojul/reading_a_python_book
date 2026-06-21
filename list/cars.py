cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True) #sort es para ordernar albeticamente (a-z) y con reverse=True de z-a 
print(cars)

#sorted() function
cars2 = ['bmw', 'audi', 'toyota', 'subaru']
print('here is the original list:')
print(cars2)

print("\nHere is the sorted list:")
print(sorted(cars2))

print("\n here is the original list again:")
print(cars2)

cars2.reverse()
print(cars2 )

print(len(cars2))