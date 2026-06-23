# Glossary: A Python dictionary can be used to model an actual dictionary.
# However, to avoid confusion, let’s call it a glossary.
# •	 Think of five programming words you’ve learned about in the previous
# chapters. Use these words as the keys in your glossary, and store their
# meanings as values.
# •	 Print each word and its meaning as neatly formatted output. You might
# print the word followed by a colon and then its meaning, or print the word
# on one line and then print its meaning indented on a second line. Use the
# newline character (\n) to insert a blank line between each word-meaning
# pair in your output.
glossary = {
    'syntaxis' : 'it is the way how we should write statement code like for loop or if-elif-else chain',
    'indentation' : 'it is a whitespace we should leave when we are using for loop or if-elif-else',
    'list' : 'it is a space where we can store serveral value to then use it how we want to',
    'dictionary' : 'it is a callection of key-value. we work with it to store some data of an object',
    'variable' : 'it is a space reserve in the memory to add a value. afterward we can use its value through the variable, calling it'
}

print(f"Syntaxis is: {glossary['syntaxis']}.\n" )
print(f"Indentation is : {glossary['indentation']}.\n")
print(f"List is {glossary['list']}.\n")
print(f"Dictionary is {glossary['dictionary']}.\n")
print(f"A variable is: {glossary['variable']}.\n")