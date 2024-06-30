import random
a=input("Enter the names seperated by comma's ")
b=a.split(",")
z=len(b)
random_choice=random.randint(0,z-1)
print(b[random_choice])
    