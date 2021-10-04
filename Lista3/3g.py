def primo (n, i=1, d=0):
    if n==i:
        return primo(n, i+1, d+1)
    else:
        if i<n:
            return primo(n, i+1, d+1) if n%i==0 else primo(n,i+1, d)
        else:
            return True if d==2 else False
print(primo(17))
