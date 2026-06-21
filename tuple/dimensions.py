dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])
#dimensions[0] = 250 no funciona en una tupla
#print(dimensions)
print("Original dimension")
for dimension in dimensions:
    print(dimension)
dimensions = (400, 100)
print("Modified dimension")
for dimension in dimensions:
    print(dimension)