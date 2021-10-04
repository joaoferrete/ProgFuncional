def imprime (n=1):
    if n==10:
        print("10")
    else:
        print(n)
        imprime(n+1)
imprime()
