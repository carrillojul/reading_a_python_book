alien_0 ={
    'color' : 'green',
    'points' : 5
}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print('You just earned ' + str(new_points) + ' points!')
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

print('-----------------------')
print('starting from 0 a dictionary')

alien_1 = {}

alien_1['color'] = 'green'
alien_1['points'] = 5

print(alien_1)
print('the alien is ' + alien_1['color'] + ".")
print('------------------------------------')


alien_2 = {'color' : 'green', 'points' : 2}

print('the alien is ' + alien_2['color'] + ".")

alien_2['color'] = 'yellow'
print('the alien is now ' + alien_2['color'] + ".")

print('------------------------------------')

alien_3 = {'x_position' : 0, 'y_position' : 25, 'speed' : 'medium'}
print('Original x-position ' + str(alien_3['x_position']))

#move the alien to the right
#determine how far to move the alien based on  its current speed
if alien_3['speed'] == 'low':
    x_increment = 1
elif alien_3['speed'] == 'medium':
    x_increment = 2
else:
    #this must be a fast alien
    x_increment = 3

#the new position is the old plus the increment
alien_3['x_position'] = alien_3['x_position'] + x_increment
print('New x-position: ' + str(alien_3['x_position']))

#for giving more position to the alien you can change
#key-value 'speed' to fast. like that the alien'll move 3 position


#here i am using the first variable from the chapter to not
#create a new one
#using del, we are deleted the key-value pair permanently
del alien_0['points']
del alien_0['x_position']
print(alien_0)