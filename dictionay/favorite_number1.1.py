people = {
    'julio' : [1,2,3],
    'valentina' : [4,5,6],
    'doris' : [7,8]
}

for key, value in people.items():
    if key == 'doris':
        print(key, 'her favorite lucky number are ' + str(value[0]) + ' and ' + str(value[1]))
    elif key == 'valentina':
        print(key +' her favorite lucky number are ' + str(value[0]) + ', ' + str(value[1]) + ' and ' + str(value[2]))
    else:
        print(key + ' her favorite lucky number are ' + str(value[0]) + ' and ' + str(value[1]))
        