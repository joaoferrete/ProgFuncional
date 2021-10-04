def propint (n):
	if 1000<=n<=9999:
		a=n//100
		b=n-a*100
		if (a+b)**2==n:
			return True
		else:
			return False
	else:
		return False
def main():
	n=int(input("Digite um número: "))
	if propint(n):
		print("Esse número possuí a propriedade interessante")
	else:
		print("Esse número não possuí a propriedade interessante")
main()
