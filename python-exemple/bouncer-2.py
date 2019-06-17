age = input("How old are you: ")
if age.isnumeric() and age:
    age = int(age)
    if age >= 21:
        print("You are good to enter and can drink!")
    elif age >= 18:
        print("You can enter, but need a wristband!")
    else:
        print("You can't come in, little one! :(")
elif not age:
    print("Please enter an age! ")
else:
    print("please enter numbers not word or chars! ")
