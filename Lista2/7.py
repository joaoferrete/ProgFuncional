def ehTriangulo (a,b,c):
	return True if (abs(b-c))<a<(b+c) and (abs(a-c))<b<(a+c) and (abs(a-b))<c<(a+b) else False
def tipoTriangulo (a,b,c):
	if ehTriangulo(a,b,c):
		if a==b and b==c:
			print("Triangulo equilátero")
		elif a==b or a==c or b==c:
			print("Triangulo Isósceles")
		else:
			print("Triangulo Escaleno")
	else:
		print("Triangulo Não Existe!")
def main():
	a=float(input("Digite a medida do lado a: "))
	b=float(input("Digite a medida do lado b: "))
	c=float(input("Digite a medida do lado c: "))
	tipoTriangulo(a,b,c)
main()
