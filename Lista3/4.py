def fibonacci (n):
    if isinstance (n, int) and n>0:
        if n>2:
            return fibonacci(n-1)+fibonacci(n-2)
        else:
            return 1
def imprimeF (n, i=1):
    if isinstance (n, int) and n>0:    
        if i==n:
            print(fibonacci(n))
        else:
            print (fibonacci(i))
            imprimeF(n, i+1)
imprimeF(13)
