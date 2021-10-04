peso = float(input())
print(f"Peso: {peso}")
idade = int(input())
print(f"Idade: {idade}")
if idade == 16 or idade == 17:
    docAutoriza = input()
    print(f"Documento de autorizacao: {docAutoriza}")
boaSaude = input()
print(f"Boa saude: {boaSaude}")
drogas = input()
print(f"Uso drogas injetaveis: {drogas}")
doacao = input()
print(f"Primeira doacao: {doacao}")

if doacao == "N":
    meses = int(input())
    print(f"Meses desde ultima doacao: {meses}")
    vezes = int(input())
    print(f"Doacoes nos ultimos 12 meses: {vezes}")

sexo = input()
print(f"Sexo biologico: {sexo}")

if sexo == "F":
    gravidez = input()
    print(f"Gravidez: {gravidez}")
    amamentando = input()
    print(f"Amamentando: {amamentando}")
    if(amamentando == "S"):
        idadeBebe = int(input())
        print(f"Meses bebe: {idadeBebe}")

impedimento = False

if peso<50:
    print("Impedimento: abaixo do peso minimo.")
    impedimento = True
if idade<16:
    print("Impedimento: menor de 16 anos.")
    impedimento = True
if 16<=idade<=18 and docAutoriza=="N":
    print("Impedimento: menor de 18 anos, sem consentimento dos responsaveis.")
    impedimento = True
if idade>60 and doacao == "S":
    print("Impedimento: maior de 60 anos, primeira doacao.")
    impedimento = True
if idade>69:
    print("Impedimento: maior de 69 anos.")
    impedimento = True
if boaSaude == "N":
    print("Impedimento: nao esta em boa saude.")
    impedimento = True
if drogas == "S":
    print("Impedimento: uso de drogas injetaveis.")
    impedimento = True
if doacao == "N" and meses < 2 and sexo == "M":
    print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
    impedimento = True
if doacao == "N" and vezes >= 4 and sexo == "M":
    print("Impedimento: numero maximo de doacoes anuais foi atingido.")
    impedimento = True
if doacao == "N" and meses < 3 and sexo == "F":
    print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
    impedimento = True
if doacao == "N" and vezes >= 3 and sexo == "F":
    print("Impedimento: numero maximo de doacoes anuais foi atingido.")
    impedimento = True
if sexo == "F" and gravidez == "S":
    print("Impedimento: gravidez.")
    impedimento = True
if sexo == "F" and amamentando == "S" and idadeBebe<12:
    print("Impedimento: amamentacao.")
    impedimento = True
if impedimento == False:
    print("Procure um hemocentro.")