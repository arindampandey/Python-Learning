marks = {
    "Ram" : 45,
    "Shyam" : 99,
    "Rohan" : 23,
    "list" : [1,2,3]
}

print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"Ram" : 55 , "Harish" : 92}) # New keys with their respective values will be added and the previous will be updated 
print(marks)

# print(marks.get("Shiva")) // Output : None

# Output is same in both situations if the key is present in the dictionary...
print(marks.get("Rohan"))
print(marks["Rohan"]) 

# IF the key is not present then...
print(marks.get("Rohan2")) # It will return None 
# print(marks["Rohan2"]) # It will throw an error 

# To clear a dictionary
# marks.clear()
print(marks)

# To copy a dictionary
new = marks.copy()
print(new)

# Pop operation
value = new.pop("Rohan",)
print(value)
print(new)

