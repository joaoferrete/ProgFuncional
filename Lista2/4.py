def ritmo (h,m,s,k):
	mi=(h*60)+m+(s/60)
	r=mi//k
	s=(((mi/k)-r)*60)
	print("Ritmo: {:02.0f}:{:02.0f} Min/KM".format(r,s))
def main():
	print("TEMPO DO CORREDOR")
	h=int(input("Horas: "))
	m=int(input("Minutos: "))
	s=int(input("Segundos: "))
	k=float(input("Distancia: "))
	ritmo (h,m,s,k)
main()
