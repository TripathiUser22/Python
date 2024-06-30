ans=0
n=int(input("Enter the Number "))
while (n!=0):
    d=n%10
    ans=ans+d
    n=n//10   
print(ans)