s1 = {1,2,3,4,77}
s2 = {2,7,9,77}

print(s1.union(s2))
print(s1.intersection(s2))

print({1,3}.issubset(s1))

print(s1.issuperset({1,2}))