print("Ritmo médio em uma corrida")
a=int(input("Digite o tempo total gasto na corrida (em min): "))
b=int(input("Digite a distância percorrida (em km) :"))
r=a//b
s=int(((a%b)/10)*60)
print("Ritmo Médio do corredor: {0:01}:{1} min/km".format(r,s))
