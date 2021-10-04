def div (n, b=1):
    if n==b:
        return 1
    else:    
        if n%b==0:
            return 1+div(n, b+1)
        return div(n, b+1)
print(div(18))
