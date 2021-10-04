def converteHoras(min):
    horas = min // 60
    min = min % 60
    return horas, min

def tempoNecessario(sexo, idade):
    if sexo == "m" or sexo == "M":
        tempo = 180
    else:
        tempo = 210
    
    if 35<=idade<=39:
        tempo +=5
    elif 40<=idade<=44:
        tempo +=10
    elif 45<=idade<=49:
        tempo +=20
    elif 50<=idade<=54:
        tempo +=25
    elif 55<=idade<=59:
        tempo +=35
    elif 60<=idade<=64:
        tempo +=50
    elif 65<=idade<=69:
        tempo +=65
    elif 70<=idade<=74:
        tempo +=80
    elif 75<=idade<=79:
        tempo +=95
    elif 80<=idade:
        tempo +=110
    return tempo

def conseguiuIndice(idade, tempo, sexo):
    tempoNes = tempoNecessario(sexo, idade)
    hrsNes, minNes = converteHoras(tempoNes)
    print(f"Tempo necessario: {hrsNes:02}h {minNes:02}min")
    if tempo<=tempoNes:
        print("Conseguiu indice? SIM")
        hrs, min = converteHoras(tempoNes - tempo)
        if sexo == "m" or sexo == "M":
            print(f"O corredor correu {hrs:02}h {min:02}min abaixo do indice")
        else:
            print(f"A corredora correu {hrs:02}h {min:02}min abaixo do indice")
    else:
        print("Conseguiu indice? NAO")
        hrs, min = converteHoras(tempo - tempoNes)
        if sexo == "m" or sexo == "M":
            print(f"O corredor correu {hrs:02}h {min:02}min acima do indice")
        else:
            print(f"A corredora correu {hrs:02}h {min:02}min acima do indice")

def main():
    tempo = int(input())
    idade = int(input())
    sexo = input()

    hrs, min = converteHoras(tempo)
    if sexo == "m" or sexo == "M": print(f"Tempo do corredor: {hrs:02}h {min:02}min")
    else: print(f"Tempo da corredora: {hrs:02}h {min:02}min")
    conseguiuIndice(idade, tempo, sexo)

main()
