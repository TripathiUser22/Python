pizza=input("Enter the Pizza Size (small/medium/large) ")
if(pizza=='small'):
    bill=100
    print(f"Your Bill is {bill} ")
elif(pizza=='medium'):
    bill=200
    print(f"Your Bill is {bill} ")
elif(pizza=='large'):
    bill=300
    print(f"Your Bill is {bill} ")
wantextra=input("Pepperoni for small pizza(Y/N) ")
if(wantextra=='Y'):
    bill=bill+30
print(f"Now Your Total Bill is {bill} ")
wantextra=input("Extra cheese  for any pizza(Y/N) ")
if(wantextra=='Y'):
    bill=bill+20
print(f"Now Your Total Bill is {bill} ")
wantextra=input("Pepperoni for Medium and Large pizza(Y/N) ")
if(wantextra=='Y'):
    bill=bill+50
print(f"Now Your Total Bill is {bill} ")
    
