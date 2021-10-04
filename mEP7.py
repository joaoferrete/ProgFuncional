def leituraVotos(nleitura, ncandidatos, lista, i=0):
    if(i==nleitura): return lista
    voto = int(input())
    if voto<=ncandidatos:
        lista[voto][1]+=1
    else:
        lista[ncandidatos+1][1]+=1
    return leituraVotos(nleitura, ncandidatos, lista, i+1)


def leituraCandidatos(n, lista, i=1):
    if(i>n): return lista
    nome = input()
    lista += [[nome, 0]]
    return leituraCandidatos(n, lista, i+1)

def imprimeVotos(lista, i=1):
    if(i==len(lista)-1):
        print(f"Brancos: {lista[0][1]}")
        print(f"Nulos: {lista[i][1]}")
        return
    else:
        print(f"{lista[i][0]}: {lista[i][1]}")
    imprimeVotos(lista, i+1)

def vencedor(lista, i=0, maior=-1):
    if i==len(lista):
        print(f"Vencedor(a): {lista[maior][0]}")
        return
    if lista[i][1] > lista[maior][1]:
        maior = i
    vencedor(lista, i+1, maior)

def main():
    ncandidato = int(input())
    lista = [["Brancos", 0]]
    lista = leituraCandidatos(ncandidato, lista)
    lista+=[["Nulos", 0]]
    nVotos = int(input())
    lista = leituraVotos(nVotos, ncandidato, lista)
    imprimeVotos(lista)
    vencedor(lista)

main()