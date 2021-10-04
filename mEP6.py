def imprimeRetangulo(l, a, c, i=1):
    if(i>a): return
    if i==a or i==1:
        print(c*l)
    elif i<a:
        print(c+(" "*(l-2))+c)
    imprimeRetangulo(l, a, c, i+1)

def imprimeParalelogramo(l, a, c, i=1):
    if(i>a): return
    if i==a or i==1:
        print((" "*(i-1)) + c*l)
    elif i<a:
        print((" "*(i-1)) + c + (" "*(l-2)) + c)
    imprimeParalelogramo(l, a, c, i+1)

def imprimeEquilatero(h, c, i=1, esp=1):
    aux=h-i
    if i>h: return
    if i==1:
        print(" "*aux + c)
    elif i==h:
        print(c*((h*2)-1))
    else:
        print(" "*aux + c + esp*" " + c)
        esp+=2
    imprimeEquilatero(h, c, i+1, esp)

def imprimeRetanguloE(h, c, i=1):
    if(i>h): return
    if i==1:
        print(c)
    elif i==h:
        print(c*h)
    else:
        print(c + (i-2)*" " + c)
    imprimeRetanguloE(h, c, i+1)

def imprimeRetanguloD(h, c, i=1):
    if(i>h): return
    if i==1: print((h-i)*" " + c)
    elif i==h: print(c*h)
    else: print((h-i)*" " + c + (i-2)*" " + c)
    imprimeRetanguloD(h, c, i+1)

def main():
    obj = input()

    if(obj == "R"):
        l = int(input())
        a = int(input())
        c = input()
        if(l<=0 or a<=0):
            print("Medida invalida.")
            return
        imprimeRetangulo(l, a, c)
    elif(obj == "P"):
        l = int(input())
        a = int(input())
        c = input()
        if(l<=0 or a<=0):
            print("Medida invalida.")
            return
        imprimeParalelogramo(l, a, c)
    elif obj == "TE":
        h = int(input())
        c = input()
        if(h<=0):
            print("Medida invalida.")
            return
        imprimeEquilatero(h, c)
    elif obj == "TRE":
        h = int(input())
        c = input()
        if(h<=0):
            print("Medida invalida.")
            return
        imprimeRetanguloE(h, c)
    elif obj == "TRD":
        h = int(input())
        c = input()
        if(h<=0):
            print("Medida invalida.")
            return
        imprimeRetanguloD(h, c)
    else:
        print("Objeto invalido.")

main()