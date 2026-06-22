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