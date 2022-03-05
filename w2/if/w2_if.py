print("What is your name?")
n = input()
if len(n) > 8:
    print("You have a long name. Can I use a nickname?")
elif len(n) <=4:
    print("You have a super-short name")
elif n == "Martha":
    print("Why did you say that name?")
else:
    print("Nice to meet you!")
    
print("Welcome to the session")