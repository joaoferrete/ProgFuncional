import math
x=float(input("Digite um número: "))
if x<=1:
	print("O resultado é {}".format(math.log(x)))
elif 1<x<=2:
	print("O resultado é {}".format(math.log10(x)+math.sqrt(x)))
elif 2<x<=5:
	print("O resultado é {}".format(x**2+(math.e**x)))
else:
	print("O resultado é {}".format((x**(x/2))+(math.log2(x))))
