# WAP to check a post is talking about india or not

post = input("Enter the post : ")

if("India".lower() in post.lower()):
    print("This post is talking about India!")

else:
    print("This post is not talking about India!")