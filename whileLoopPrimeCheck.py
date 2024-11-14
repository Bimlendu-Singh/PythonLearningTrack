n=int(input("Enter number to check prime or not: "))
i=2
count=0

while i<=n/2:
    if(n%i==0):
        count+=1
        break
    i+=1

if(count>0):
    print("Number :",n," is not prime")
else:
    print("Number :",n," is prime")
