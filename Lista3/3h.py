def somaDigitos (n, i=1):
    if i>n:
        return 0
    else:
        return (n//i-((n//(i*10))*10)) + somaDigitos(n, i*10)
print(somaDigitos(12345678910))
