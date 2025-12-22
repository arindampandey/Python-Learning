# Create an empty dictionary . Allow 4 friends to enter their favourite language as value and use key as their names. Assume that their names are unique.
d = {}

name = input("Enter friend's name : ")
lang = input("Enter the language : ")
d.update({name : lang})

name = input("Enter friend's name : ")
lang = input("Enter the language : ")
d.update({name : lang})

name = input("Enter friend's name : ")
lang = input("Enter the language : ")
d.update({name : lang})

name = input("Enter friend's name : ")
lang = input("Enter the language : ")
d.update({name : lang})

print(d)
