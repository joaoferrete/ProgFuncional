print("DIGITE A DATA DE NASCIMENTO:")
d1=int(input("Dia: "))
m1=int(input("Mês: "))
a1=int(input("Ano: "))
print("DIGITE A DATA ATUAL:")
d2=int(input("Dia: "))
m2=int(input("Mês: "))
a2=int(input("Ano: "))

idd=a2-a1
if m1>m2 or (m1==m2 and d1>d2):
	idd-=1
print("IDADE: {}".format(idd))
