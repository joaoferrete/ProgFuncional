print("VEJA SE VOCÊ FOI APROVADO OU NÃO")
x=int(input("Digite a nota da prova 1: "))
y=int(input("Digite a nota da prova 2: "))
z=int(input("Digite a nota da prova 3: "))
media=(x+y+z)/3
if media>=7:
	print("APROVADO! SUA MÉDIA FOI {}".format(media))
else:
	print("VOCÊ ESTÁ DE PROVA FINAL! SUA MÉDIA PARCIAL FOI {}".format(media))
	t=int(input("DIGITE A NOTA DA PROVA FINAL: "))
	mediafinal=(media+t)/2
	if mediafinal>=5:
		print("APROVADO! SUA MÉDIA FINAL É {}".format(mediafinal))
	else:
		print("REPROVADO! SUA MÉDIA FINAL É {}".format(mediafinal))
		print("TE VEJO ANO QUE VEM!")
