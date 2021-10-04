def sq2m (a,b,c):
	if a>b and c>b:
		return (a**2)+(c**2)
	elif a>c and b>c:
		return (a**2)+(b**2)
	elif b>a and c>a:
		return (b**2)+(c**2)
print(sq2m(4,5,6))
