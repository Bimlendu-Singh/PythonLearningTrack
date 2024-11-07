x=complex(input("Enter a complex number, e.g 2+4j: "))
realPart = x.real
imagPart = x.imag

if x.real>x.imag:
    print("Real part ",realPart," is Greater!")
elif x.real<x.imag:
    print("Imaginary part ",imagPart," is Greater!")
else:
    print("Both are equal")
