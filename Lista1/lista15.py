print("Digite o tempo de natação: ")
h1=int(input("horas :"))
m1=int(input("minutos :"))
s1=int(input("segundos :"))

print("Digite o tempo de transição (natação -> pedal)")
ht1=int(input("horas :"))
mt1=int(input("minutos :"))
st1=int(input("segundos :"))

print("Digite o tempo do pedal: ")
hp=int(input("horas :"))
mp=int(input("minutos :"))
sp=int(input("segundos :"))

print("Digite o tempo de transição Pedal-> corrida: ")
ht2=int(input("Horas: "))
mt2=int(input("Minutos: "))
st2=int(input("SEgundos: "))

print("Digite o tempo de corrida: ")
hc=int(input("Horas: "))
mc=int(input("Minutos: "))
sc=int(input("Segundos: "))

st=(s1+st1+sp+st2+sc)
if st>=60:
	mt=(m1+mt1+mp+mt2+mc+st//60)
	st=st-(60*(st//60))
else:
	mt=(m1+mt1+mp+mt2+mc)
if mt>=60:
	ht=(h1+ht1+hp+ht2+hc+mt//60)
	mt=mt-(60*(mt//60))
else:
	ht=(h1+ht1+hp+ht2+hc)
print("TEMPO TOTAL DO ATLETA: {}h {}min {}seg".format(ht, mt, st))
