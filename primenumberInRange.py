# First taking range lower and upper so to find prime number between them.
lowerRange = int(input("Enter you lower range: "))
upperRange = int(input("Enter you upper range: "))

i=2
count=0

#Loop for finding prime number between range
while lowerRange<=upperRange:  #Let 4 and 20 are the lower and upper range 
    count=0
    i=2
    while i<(lowerRange//2):   #e.g 2<2//2 i.e,0
        if(lowerRange%i==0):
            count+=1
            break
        i+=1
    # Wheneve count is 0 that it is prime not divisible by any number it will pe printed
    if(count==0):
        print(lowerRange," ")

    lowerRange+=1
        
        
