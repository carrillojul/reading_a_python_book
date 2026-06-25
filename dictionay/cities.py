# Cities: Make a dictionary called cities. Use the names of three cities as
# keys in your dictionary. Create a dictionary of information about each city and
# include the country that the city is in, its approximate population, and one fact
# about that city. The keys for each city’s dictionary should be something like
# country, population, and fact. Print the name of each city and all of the information you have stored about it.

cities = {
    'medellin' : {
        'fact' : 'the most popular city in colombia',
        'country' : 'colombia',
        'population' : 5000000
    },
    'maracaibo' : {
        'fact' : 'this city has the highest weather',
        'country': 'venezuela',
        'population' : 6000000
    },
    'barranquilla' : {
        'fact' : 'this city and maracaibo are so similar',
        'country' : 'colombia',
        'population' : '4000000'
    }
    }

for city, info_0 in cities.items():
        city_fact = info_0['fact']
        city_county = info_0['country']
        city_population = info_0['population']
        print(city,'\n\t', city_fact)