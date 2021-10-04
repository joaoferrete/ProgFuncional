def imprime (n, i=1):
    if i==n:
        print (n)
    else:
        print (i)
        imprime(n, i+1)
        
imprime(100)
