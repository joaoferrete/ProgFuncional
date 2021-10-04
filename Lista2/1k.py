def ascendente (n):
	if 100<=n<=999:
		a=n//100
		b=n//10-a*10
		c=n-(a*100+b*10)
		return True if a<b and b<c else False
	else:	
		print("ERRO")
		return False
print(ascendente(143))
