######################################################
# Programção I / Programação Funcional (2022/1)
# miniEP3 - Ironman
# Nome:
# Matrícula:
######################################################

######################################################
# LEMBRE-SE:
# - Não é permitido usar estruturas de repetição,
#   funções impuras e operações que não sejam do
#   Paradigma Funcional.
# - Você NÃO pode usar variáveis globais;
# - Não use funções recursivas (não há necessidade);
# - Caso precise, você PODE criar outras funções;
# - Evite ao máximo a replicação de código. 
#   Códigos que não atendam a esse requisito 
#   valerão 50% da pontuação;
######################################################

def converteHoras(min):
    horas = min // 60
    min = min % 60
    return horas, min

def indice(sexo, idade):
    if sexo == "m" or sexo == "M": tempo = 480
    else: tempo = 490

    if 30 <= idade <= 34:
        tempo += 10
    elif 35 <= idade <= 39:
        tempo += 25 if sexo == "m" or sexo == "M" else 30
    elif 40 <= idade <= 44:
        tempo += 35 if sexo == "m" or sexo == "M" else 50
    elif 45 <= idade <= 49:
        tempo += 50 if sexo == "m" or sexo == "M" else 70
    elif 50 <= idade <= 54:
        tempo += 60 if sexo == "m" or sexo == "M" else 90
    elif 55 <= idade <= 59:
        tempo += 75 if sexo == "m" or sexo == "M" else 110
    elif 60 <= idade <= 64:
        tempo += 90 if sexo == "m" or sexo == "M" else 140
    elif 65 <= idade <= 69:
        tempo += 110 if sexo == "m" or sexo == "M" else 170
    elif 70 <= idade <= 74:
        tempo += 140 if sexo == "m" or sexo == "M" else 215
    elif 75 <= idade <= 79:
        tempo += 180 if sexo == "m" or sexo == "M" else 260
    elif 80 <= idade:
        tempo += 240 if sexo == "m" or sexo == "M" else 320

    return tempo

def verifSexo(sexo):
    if sexo == "m" or sexo == "M":
        return "do", "O"
    else:
        return "da", "A"


def main():
    # Faça a leitura dos dados;
    # Faça todo o processamento dos dados (você PODE criar/usar outras funções) e imprima as informações necessárias;
    # Deixe todas as variáveis dentro de alguma função. Uma variável fora de uma função, significa 
    #    que ela é global (leia as observações 1 e 2)
    sexo = input()
    idade = int(input())
    tempoAtleta = 0
    tempoAtleta += int(input())
    tempoAtleta += int(input())
    tempoAtleta += int(input())
    tempoAtleta += int(input())
    tempoAtleta += int(input())
    tempoNecessario = indice(sexo, idade)

    ligacao, artigo = verifSexo(sexo)

    h, m = converteHoras(tempoAtleta)
    print(f"Tempo {ligacao} atleta: {h:02d}h {m:02d}min")
    h, m = converteHoras(tempoNecessario)
    print(f"Tempo necessario: {h:02d}h {m:02d}min")
    h, m = converteHoras(abs(tempoNecessario - tempoAtleta))

    if tempoAtleta > tempoNecessario:
        print("Conseguiu indice? NAO")
        print(f"{artigo} atleta terminou a prova {h:02d}h {m:02d}min acima do indice")
    else:
        print("Conseguiu indice? SIM")
        print(f"{artigo} atleta terminou a prova {h:02d}h {m:02d}min abaixo do indice")



main()
