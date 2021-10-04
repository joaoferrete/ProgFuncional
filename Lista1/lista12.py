x=float(input("Digite o numero de lados: "))
y=float(input("Digite a medida do lado: "))
if x==3:
	print("TRIANGULO! \nO perímetro é {}".format(3*y))
elif x==4:
	print("QUADRADO \nA área é {}".format(y*y))
elif x==5:
	print("PENTÁGONO")
else:
	print("POLIGONO NÃO IDENTIFICADO!")
