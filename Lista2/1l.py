def palindromo (n):
	if n>=1000 and n<=9999:
		a=n//1000
		b=n//100-a*10
		c=n//10-(a*100+b*10)
		d=n-(a*1000+b*100+c*10)
		if a==d and b==c:
			return True
		else:
			return False
	else:
		print("ERRO")
		return False
print(palindromo(1221))
