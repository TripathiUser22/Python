your_name=input("Enter Your Name ")
Her_name=input("Enter Her Name ")
combine=your_name+Her_name
a=combine.lower()
t=combine.count('t')
r=combine.count('r')
u=combine.count('u')
e=combine.count('e')
true=t+r+u+e
l=combine.count('l')
o=combine.count('o')
v=combine.count('v')
e=combine.count('e')
love=l+o+v+e
Love=love+true
print(f"Your Love score is {Love} ")
if(Love>=3):
 print("Your love is successfull and you are true lover")
else:
    print("You are not true lover")

