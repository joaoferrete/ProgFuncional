def naturais (a, b):
    if a>=0:
        if a==b:
            print(b)
        else:
            print (a)
            naturais(a+1, b)
    else:
        naturais(0, b)
naturais(-55,55)
