a=float(input("Digite a medida do lado a: "))
b=float(input("Digite a medida do lado b: "))
c=float(input("Digite a medida do lado c: "))
if (abs(b-c))<a<(b+c) and (abs(a-c))<b<(a+c) and (abs(a-b))<c<(a+b):
	print("O TRIANGULO EXISTE!!")
	if a==b and b==c:
		print("Triangulo equilátero")
	elif a==b or a==c or b==c:
		print("Triangulo Isósceles")
	else:
		print("Triangulo Escaleno")
else:
	print("TRIANGULO NÃO EXISTE!!")
