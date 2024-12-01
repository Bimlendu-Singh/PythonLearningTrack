lowerRange = int(input("Enter you lower range: "))
upperRange = int(input("Enter you upper range: "))

i=2
count=0


while lowerRange<=upperRange:
    count=0
    i=2
    while i<(lowerRange//2):
        if(lowerRange%i==0):
            count+=1
            break
        i+=1
    if(count==0):
        print(lowerRange," ")

    lowerRange+=1
