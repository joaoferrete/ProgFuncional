print("VERIFIQUE SE O NÚMERO É UM PALÍNDROMO!")
x=int(input("Digite um número entre 1000 e 9999: "))
if x<1000 or x>9999:
	print("ERRO! NÚMERO FORA DO INTERVALO SOLICIDADO!")
else:
	a=x//1000
	b=x//100-a*10
	c=x//10-(a*100+b*10)
	d=x-(a*1000+b*100+c*10)
	if a==d and b==c:
		print("{} É UM PALÍNDROMO!".format(x))
	else:
		print("{} NÃO É UM PALÍNDROMO!".format(x))
