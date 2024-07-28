name = input("please enter your name: ")

if len(name) <= 3:
    print("Name should contain more than 3 letters")
elif len(name) >= 10:
    print("Name should contain less than 10 letters")
else:
    print("Name looks good")