# WAP to replace a list of such words that should be censored.
words = ["Donkey" , "bad" , "Ganda"]

with open("file.txt" , "r") as f:
    content = f.read()

for word in words:
    content = content.replace(word , "#" * len(word))

with open("file.txt" , "w") as f :
    f.write(content)