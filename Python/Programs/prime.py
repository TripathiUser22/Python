n=int(input("Enter the Number to check "))
i=2
for i in range(2,n):
    if(n%i==0):
        print("It is not prime no")
        break
    else:
      print("It is prime number")
      break
    