items = ["Apple","Orange",5,2.21,False,"Akash","Physics"]
print(items)
items.append("Hello") # To add elements at the end of the list
print(items)

l1 = [1,22,2.11,6,43,19,33]
# l1.sort()
# l1.reverse()
l1.insert(3,22222) # l1.insert(index,object)
print(l1)

value = l1.pop(3)
print(value)
print(l1)

l1.remove(2.11)
print(l1)
