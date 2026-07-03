# Dream Vacation: Write a program that polls users about their dream
# vacation. Write a prompt similar to If you could visit one place in the world,
# where would you go? Include a block of code that prints the results of the poll.

prompt = "if you could visit one place in the world where would you go?"


while True:
    answer = input(prompt)
    if answer == quit:
        break
    else:
        print("I can see that you'd love to travel: " + answer)