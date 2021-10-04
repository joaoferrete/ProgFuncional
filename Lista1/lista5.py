x=int(input("Digite um número: "))
contapar=0
contaimpar=0
somapar=0
somaimpar=0
if x%2==0:
    contapar+=1
    somapar+=x
else:
    contaimpar+=1
    somaimpar+=x
x=int(input("Digite um número: "))
if x%2==0:
    contapar+=1
    somapar+=x
else:
    contaimpar+=1
    somaimpar+=x
x=int(input("Digite um número: "))
if x%2==0:
    contapar+=1
    somapar+=x
else:
    contaimpar+=1
    somaimpar+=x
x=int(input("Digite um número: "))
if x%2==0:
    contapar+=1
    somapar+=x
else:
    contaimpar+=1
    somaimpar+=x
if contapar!=0:
    mediapar=somapar/contapar
    print("Foram digitados {} números pares. \nA soma deles é {} e a média é {}".format(contapar,somapar,mediapar))
else:
    print("Não foram digitados números pares")
if contaimpar!=0:
    mediaimpar=somaimpar/contaimpar
    print("Foram digitados {} números ímpares. \nA soma deles é {} e a média é {}".format(contaimpar,somaimpar,mediaimpar))
else:
    print("NÃO FORAM DIGITADOS NÚMEROS IMPARES")
