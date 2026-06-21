#the exercise was 1'000.000, but I decided make it simpler because that mount was alot
number = []
for i in range(1,1001):
    number.append(i)
    mini = min(number)
    maxi = max(number)
    suma = sum(number)

print(f"El minimo es: {mini}. El maximo es: {maxi}. y la suma es: {suma}" )

#another way to use or do this exercise
even_number = list(range(1,1001,1))

tiny = min(even_number)
big = max(even_number)
plus = sum(even_number)
print(f"I just wanna know the smallest, tiniest and sumary of the list. Min: {tiny}. Max:  {big}. the sum of the list: {plus}")