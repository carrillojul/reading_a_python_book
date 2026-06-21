answer = 17
if answer != 42:
    print('that is not the correct answer. please try again!')

#age = 19
#age < 21
# True
#age <= 21
#True
#age > 21
#False
#age >= 21  
#False

#multiple condition
age_0 = 22
age_1 = 18
if age_0 >= 21  and age_1 >= 21:
    print('True')
    #output is false because one condition was false.

age_1 = 22

if age_0 >= 21 and age_1 >= 21:
    print('True')
    #In this case the output is true because of both condition was True
print('----------------------')
age_3 = 22
age_4 = 18

#In this case we used the same idea above
#but I used different variable to not confuse with
#the first comparison multiple checking
if (age_3 >= 21) or (age_4 >= 21):
    print('True')

age_3 = 18

if (age_3 >= 21) or (age_4 >= 21):
    print('True')
