# Favorite Places: Make a dictionary called favorite_places. Think of three
# names to use as keys in the dictionary, and store one to three favorite places
# for each person. To make this exercise a bit more interesting, ask some friends
# to name a few of their favorite places. Loop through the dictionary, and print
# each person’s name and their favorite places.

viajeros = {
    'doris' : ['maracaibo', 'caracas'],
    'valentina' : ['cancun', 'cartage', 'santa marta'],
    'julio' : ['maracaibo', 'medellin']
}


for key, value in viajeros.items():
    if key == 'julio':
         print(key.title(), 'has only traveled to ', value[0].title(), 'and', value[1].title(), '\n')
    elif key == 'valentina':
          print(key.title(), 'has had many trips such as', value[0].title(), value[1].title(), value[2].title(), '\n')
    else:
         print(key.title(), 'travel a lot for bussiness to ', value[0].title(), 'and', value[1].title(), '\n')