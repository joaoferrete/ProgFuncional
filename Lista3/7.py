def fat (n):
    if n==0:
        return 1
    else:
        return n*fat(n-1)
def euler (n):
    if n==0:
        return 1/fat(0)
    else:
        return (1/fat(n-1))+euler(n-1)
def main():
    x=int(input("Digite o numero de termos para o calculo: "))
    print("Números de termos: {0} \nResultado: {1:.6}".format(x, euler(x)))
main()
