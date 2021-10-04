def palindromo (n=1000):
    if 1000<=n<=9999:
        a=n//1000
        b=n//100-a*10
        c=n//10-(a*100+b*10)
        d=n-(a*1000+b*100+c*10)
        if a==d and b==c:
	        print (n)
	        if b!=9:
	            n+=109
        palindromo(n+1)
palindromo()
