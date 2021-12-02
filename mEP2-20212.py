a = int(input())
b = int(input())
c = int(input())

A=0
B=0
C=0


if(a > b and a > c):
    A = a
    if(b > c):
        B = b
        C = c
    else:
        B = c
        C = b
elif(b > a and b > c):
    A = b
    if(a > c):
        B = a
        C = c
    else:
        B = c
        C = a
else:
    A = c
    if(a > b):
        B = a
        C = b
    else:
        B = b
        C = a

if(A <= 0 or B <= 0 or C <= 0):
    print("Valores invalidos.")
elif (A >= B + C) or (B >= A + C) or (C >= A + B):
    print("Valores nao podem formar um triangulo.")
else:
    if(A==B and A==C):
        print("Triangulo equilatero.")
    elif(A==B or A==C or B==C):
        print("Triangulo isosceles.")
    else:
        print("Triangulo escaleno.")

    if(A*A < B*B + C*C):
        print("Triangulo acutangulo.")
    elif(A*A > B*B + C*C):
        print("Triangulo obtusangulo.")
    else:
        print("Triangulo retangulo.")