my_favorite_foods = ['pizza', 'falafel', 'carrot cake']
friend_foods = my_favorite_foods[:]
print(f"My favorite food is are {my_favorite_foods}")

print(f"\nMy friend's favorite food are: {friend_foods}")

my_favorite_foods.append('canoli')
friend_foods.append('ice cream')
print(f"My favorite food is are {my_favorite_foods}")

print(f"\nMy friend's favorite food are: {friend_foods}")
print("----------------------------")

#this doesn't work
my_friend_food = my_favorite_foods
my_favorite_foods.append('canela')

print(f"my favorite foods are: {my_favorite_foods}")
print(f"\nmy friend's favorite foods are: {my_friend_food}")

print("---------------------")
print("The first three are: ")
print(my_favorite_foods[:3])
print("----------------------")
print("Three item from the middle are: ")
print(my_favorite_foods[1:4])
print("----------------------")
print("The last three are: ")
print(my_favorite_foods[2:5])

for i in my_favorite_foods:
    print(i)

print("---------------------")
for i2 in my_friend_food[:5]:
    print(i2)

