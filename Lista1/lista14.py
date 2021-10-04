a=int(input("Digite o primeiro ângulo: "))
b=int(input("Digite o segundo ângulo: "))
c=int(input("Digite o terceiro ângulo: "))
if a+b+c==180:
	print("TRIÂNGULO EXISTE!")
	if a==90 or b==90 or c==90:
		print("Triangulo Retângulo")
	elif a>90 or b>90 or c>90:
		print("Triangulo Obtusângulo")
	elif a<90 and b<90 and c<90:
		print("Triângulo Acutângulo")
else:
	print("Triângulo Não Existe!")
