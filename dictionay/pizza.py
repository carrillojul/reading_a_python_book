#store information about pizza being ordered
pizza = {
    'crust' : 'thick',
    'toppings' : ['mushroom', 'extra cheese']
}
                        #under this comment
#sumarize the order.  we access to pizza value in 'crust'   
print('You ordered a ' + pizza['crust'] + '-crust pizza'
      + ' with the following topping:')

for topping in pizza['toppings']: #here we make a loop on 
    print('\t' + topping)         #toppings pizza key that is a list. that's why we make that syntax
  