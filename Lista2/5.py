def delta (a,b,c):
	return b**2-4*a*c
def raizes (a,b,c):
	from math import sqrt
	d=delta (a,b,c)
	if d<0:
		print("A EQUAÇÃO NÃO EXISTE RAIZES REAIS")
	elif d==0:
		print("AS RAIZES SÃO ÍGUAIS! \n Elas são iguais à {}".format((-b+sqrt(d))/(2*a))
	else:
		print("AS RAIZES SÃO {} E {}".format(((-b+sqrt(d))/(2*a)), ((-b-sqrt(d))/(2*a))))
def main():
	a=int(input("Digite o valor de A da equação: "))
	b=int(input("Digite o valor de B da equação: "))
	c=int(input("Digite o valor de C da equação: "))
	raizes(a,b,c)
main()
