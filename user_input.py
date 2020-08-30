# first way
# name = input ("enter your name :- ")
# age = input ("enter your age :- ")
# print ("Hallo "+ name + "your age is "+age)
# second way
# name, age = input("enter your name and age :- ").split(",")
# print("Hallo {} your age is {} ".format(name, age))
# third way
name, age = input("enter your name and age :- ").split(",")
print (f"Hallo {name} your age is {age}")
