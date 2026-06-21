guests = ['julio', 'cesar', 'porta']

message_julio = "I would like to invite you to my party tonight I hope yo'll come. \nto: " + guests[0].title() + "."
message_cesar = "you are invited to my birthday, don't be late. \nto: " + guests[1].title() + "."
message_porta = "you are the most important person I want you to come. \nto: " + guests[2].title() + "."
print(message_julio)
print(message_cesar)
print(message_porta)

poppe_guest = guests.pop(0)
print('dear friend, I coundnt get there. I had a problem to attend. \nfrom: ' + poppe_guest + ".")
print(guests)

guests.insert(0, 'valen')
print(guests)

new_invitation1 = "hello, dear " + guests[0].title() + "I wanna invite you to my party"
new_invitation2 = "I hope you are well, I wanna know if you really gonna come to my party tonight. to: " + guests[1].title() + "."
new_invitation3 = "I am remembering you my party is tonigth, " + guests[2].title()

print(new_invitation1)
print(new_invitation2)
print(new_invitation3)

print("I have found a bigger table, I hope someone else wanna come to my dinner party")

guests.insert(3, "nicoll")
guests.insert(0, 'pedri')
guests.append("gavi")

print("I am remembering you my party is tonigth, " + guests[0].title())
print("I am remembering you my party is tonigth, " + guests[1].title())
print("I am remembering you my party is tonigth, " + guests[2].title())
print("I am remembering you my party is tonigth, " + guests[3].title())
print("I am remembering you my party is tonigth, " + guests[4].title())
print("I am remembering you my party is tonigth, " + guests[5].title())

print("sorry, but I can invite only two people more")

popped_guests1 = guests.pop(1)
popped_guests2 = guests.pop(1)
popped_guests3 = guests.pop(2)
popped_guests4 = guests.pop(2)

print("I am sorry I can not invite them to dinner." + popped_guests1.title())
print("I am sorry I can not invite them to dinner." + popped_guests2.title())
print("I am sorry I can not invite them to dinner." + popped_guests3.title())
print("I am sorry I can not invite them to dinner." + popped_guests4.title())

print("You are still invited to my dinner " + guests[0])
print("You are still invited to my dinner " + guests[1])

del guests[0]
del guests[0]


print(guests)

