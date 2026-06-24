favorite_language = {
    'jen' : ['python', 'ruby'],
    'sarah' : ['c'],
    'edward' : ['ruby', 'go'],
    'phil' : ['python', 'haskell']
}
for name, languages in favorite_language.items():
    if len(languages) > 1:
        print('some people has mor than 1 programming language')
    print('\n'+ name.title() + "'s favorite lenguage are:")
    for language in languages:
        print('\t' + language.title())
    print('\t'+ name + ' has ' + str(len(languages)))
