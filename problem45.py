# WAP using functions to remove given word from a list and strip it at the same time. 
def remove(l,word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["Rohan","Soham","an","Hello","Katran"]

print(remove(l,"an"))