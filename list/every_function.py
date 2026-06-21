countries = ["vietnam", "germany", "italy", "france", "spain"]
capital_letter0 = countries[0].title()
capital_letter1 = countries[1].title()
capital_letter2 = countries[2].title()
capital_letter3 = countries[3].title()
capital_letter4 = countries[4].title()

print(capital_letter0)
print(capital_letter1)
print(capital_letter2)
print(capital_letter3)
print(capital_letter4)

len_countries = len(countries)
print(len_countries)

sorted_countries = sorted(countries)
print(sorted_countries)
print(countries)

countries.sort()
print(countries)

countries.sort(reverse=True)
print(countries)

popped_country = countries.pop(1)

print(countries, ". country deleted: " , popped_country)

#countries.remove("vietnam") una manera de remover items de una lista
delete_country = "vietnam" #segunda manera
countries.remove(delete_country)
print(countries)

countries.append("colombia")
print(countries)

countries.insert(2, "spain")
print(countries)