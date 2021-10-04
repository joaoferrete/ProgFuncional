x=int(input("Digite um número entre 100 e 999: "))
if 100<=x<=999:
	a=x//100
	b=x//10-a*10
	c=x-(a*100+b*10)
	if a<b and b<c:
		print("{} É ASCENDENTE".format(x))
	else:
		print("{} NÃO É ASCENDENTE".format(x))
else:
	print("ERRO! NÚMERO FORA DO LIMITE SOLICITADO!")
