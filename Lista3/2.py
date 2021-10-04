def areaQuadrado (l):
    return l*l

def areaCirculo (r):
    from math import pi
    return pi*(r**2)

def areaHexagono (l):
    from math import sqrt
    return ((3*sqrt(3))/2)*l**2
    
def imprime (n, funcao):
    print("A Área é:", funcao(n))
imprime(4, areaQuadrado)
imprime(4, areaCirculo)
imprime(4, areaHexagono)
