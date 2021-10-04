def tipo (v):
	if isinstance(v, bool):
		print("Booleano")
	elif isinstance(v, float):
		print("Ponto Flutuante")
	elif isinstance(v, str):
		print("String")
	elif isinstance(v,int):
		print("Inteiro")
	else:
		print("Outro Tipo")
tipo(False)
