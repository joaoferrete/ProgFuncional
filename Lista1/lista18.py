ano=int(input("DIGITE O ANO: "))
if ano>=1582 and ano<=1699:
	x=22
	y=2
elif ano>=1700 and ano<= 1799:
	x=23
	y=3
elif ano>=1800 and ano<= 1899:
	x=23
	y=4
elif ano>=1900 and ano <=1999:
	x=24
	y=5
elif ano>=2000 and ano<=2099:
	x=24
	y=5
elif ano>=2100 and ano<=2199:
	x=24
	y=6
elif ano>=2200 and ano<=2299:
	x=25
	y=0
elif ano>=2300 and ano<=2399:
	x=26
	y=1
elif ano>=2400 and ano<=2499:
	x=25
	y=1
else:
	x=0
	y=0
a=ano%19
b=ano%4
c=ano%7
d=(19*a+x)%30
e=(2*b+4*c+6*d+y)%7
p=(22+d+e)
p1=(d+e-9)
p2=(p1-7)
if x==0 and y==0:
	print("ERRO! ANO INVÁLIDO!)
elif p<=31:
	print("Em {} a páscoa foi ou será em {} de Março".format(ano, p))
elif p1<=25:
	print("Em {} a Páscoa foi ou será em {} de Abril".format(ano, p1))
else:
	print("Em {} a Páscoa foi ou será em {} de Abril".format(ano, p2))


