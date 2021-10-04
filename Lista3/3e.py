def quad (a, b, i=1):
    if b==0:
        return 1
    elif i==b:
        return a
    else:
        return a* quad(a, b, i+1)
print(quad(9,2))
