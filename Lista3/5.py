
def ehPerfeito(n, sD=0, i=1):
    if n>0 and isinstance(n, int):
        if i==n:
            if sD==n:
                return True
            else:
                return False
        else:
            if n%i==0:
                return ehPerfeito(n, sD+i, i+1)
            else:
                return ehPerfeito(n, sD, i+1)
    else:
        print("ERRO")
def perfeitos (n, i=1):
    if n>0 and isinstance(n, int):
        if ehPerfeito(i):
            if i==n:
                print (i)
            else:
                print(i)
                perfeitos(n, i+1)
        else:
            if n==i:
                print("", end="")
            else:
                perfeitos(n, i+1)
    else:
        print("ERRO")
def main():
    a=int(input("Digite um número natural"))
    perfeitos(a)
main()
