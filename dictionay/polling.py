# Polling: Use the code in favorite_languages.py (page 104).
# •	 Make a list of people who should take the favorite languages poll. Include
# some names that are already in the dictionary and some that are not.
# •	 Loop through the list of people who should take the poll. If they have
# already taken the poll, print a message thanking them for responding.
# If they have not yet taken the poll, print a message inviting them to take
# the poll.

user = {
    'jen' : 'python',
    'sarah' : 'c',
    'edward' : 'ruby',
    'julio' : 'python'
}

not_users =['miguelito', 'porta', 'jen', 'sarah', 'edward', 'julio','cesar']

for not_user in not_users:
    if not_user not in user.keys():
        print('you are invited to our poll!')
    else:
        print('thank you for taking our poll!')

