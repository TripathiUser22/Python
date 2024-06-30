Height=int(input("Enter The Height "))
if(Height>=3):
 print("Can Ride")
 age=int(input("Enter the age "))
 if(age<12):
     bill=150
     print(f"Your Bill is{bill} ")
 elif(age>12 and age<40):
     bill=250
     print(f"Your Bill is{bill} ")
 elif(age>40):
     bill=300
     print(f"Your Bill is{bill} ")
 want_photo=input("Do you Take Photo(Y/N) ")
 if(want_photo=='Y'):
     bill=bill+50
 print(f"Your Total Bill is{bill} ")
else:
 print("Can't Ride ")
 print("Thanks For visiting ")
  