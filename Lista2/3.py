def funcao (x):
	import math
	if x<=1:
		return (math.log(x))
	elif 1<x<=2:
		return (math.log10(x)+math.sqrt(x))
	elif 2<x<=5:
		return (x**2+(math.e**x))
	else:
		return ((x**(x/2))+(math.log2(x)))
print(funcao(6))
