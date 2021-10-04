from os import system , name


def limpaTela():
    if name == 'nt': system('cls')
    else: system('clear')

def menu():
    print("|-----------MENU------------|")
    print("|                           |")
    print("|1 - DEPOSITAR              |")
    print("|2 - SACAR                  |")
    print("|3 - SALDO                  |")
    print("|4 - RELATÓRIO              |")
    print("|0 - FINALIZAR              |")
    print("|                           |")
    print("|---------------------------|")
    indice = int(input("ESCOLHA UMA OPÇÂO: "))
    print("|---------------------------|")
    return indice

def deposita(n100, n50, n20, n10, n5, n2, n1):


    valor = int(input("Coloque o valor: R$ "))
    if(valor == 100): n100+=1
    elif (valor == 50): n50+=1
    elif (valor == 20): n20+=1
    elif (valor == 10): n10+=1
    elif (valor == 5): n5+=1
    elif (valor == 2): n2+=1
    elif (valor == 1): n1+=1
    elif (valor < 0): return n100, n50, n20, n10, n5, n2, n1
    else: print(f"Nota de R${valor}.00 não reconhecida")
    return deposita(n100, n50, n20, n10, n5, n2, n1)
    
def sacar(n100, n50, n20, n10, n5, n2, n1, total):
    if(total >= 100 and n100>0):
        print("R$ 100,00")
        total-=100
        n100-=1
    elif(total >= 50 and n50>0):
        print("R$ 50,00")
        total-=50
        n50-=1
    elif(total >= 20 and n20>0):
        print("R$ 20,00")
        total-=20
        n20-=1
    elif(total >= 10 and n10>0):
        print("R$ 10,00")
        total-=10
        n10-=1
    elif(total >= 5 and n5>0):
        print("R$ 5,00")
        total-=5
        n5-=1
    elif(total >= 2 and n2>0):
        print("R$ 2,00")
        total-=2
        n2-=1
    elif(total >= 1 and n1>0):
        print("R$ 1,00")
        total-=1
        n1-=1
    elif(total == 0):
        return n100, n50, n20, n10, n5, n2, n1
    return sacar(n100, n50, n20, n10, n5, n2, n1, total)

def podeSacar(n100, n50, n20, n10, n5, n2, n1, total):
    if(total >= 100 and n100>0):
        total-=100
        n100-=1
    elif(total >= 50 and n50>0):
        total-=50
        n50-=1
    elif(total >= 20 and n20>0):
        total-=20
        n20-=1
    elif(total >= 10 and n10>0):
        total-=10
        n10-=1
    elif(total >= 5 and n5>0):
        total-=5
        n5-=1
    elif(total >= 2 and n2>0):
        total-=2
        n2-=1
    elif(total >= 1 and n1>0):
        total-=1
        n1-=1
    elif total == 0:
        return True
    elif total>0:
        return False
        
    return podeSacar(n100, n50, n20, n10, n5, n2, n1, total, tentativa)

def saldo(n100, n50, n20, n10, n5, n2, n1):
    return (n100*100 + n50*50 + n20*20 + n10*10 + n5*5 + n2*2 + n1*1)

def relatorio(n100, n50, n20, n10, n5, n2, n1):
    print("Notas de R$ 100,00 : ", n100)
    print("Notas de  R$ 50,00 : ", n50)
    print("Notas de  R$ 20,00 : ", n20)
    print("Notas de  R$ 10,00 : ", n10)
    print("Notas de   R$ 5,00 : ", n5)
    print("Notas de   R$ 2,00 : ", n2)
    print("Notas de   R$ 1,00 : ", n1)

def relatorioSaque(n100, n50, n20, n10, n5, n2, n1):
    if(n100>0): print(f"{n100} x R$ 100,00")
    if(n50>0): print(f"{n50} x R$ 50,00")
    if(n20>0): print(f"{n20} x R$ 20,00")
    if(n10>0): print(f"{n10} x R$ 10,00")
    if(n5>0): print(f"{n5} x R$ 5,00")
    if(n2>0): print(f"{n2} x R$ 2,00")
    if(n1>0): print(f"{n1} x R$ 1,00")


def cofrinho(n100 =1, n50=1, n20 = 2, n10=1, n5=1, n2=1, n1=1):
    limpaTela()
    indice = menu()
    total = saldo(n100, n50, n20, n10, n5, n2, n1)
    
    if(indice == 1):
        print("INSIRA OS VALORES A SEREM DEPOSITADOS: ")
        print("DIGITE UM VALOR NEGATIVO PARA ENCERRAR")
        n100, n50, n20, n10, n5, n2, n1 = deposita(n100, n50, n20, n10, n5, n2, n1)
        total2 = saldo(n100, n50, n20, n10, n5, n2, n1)
        print(f"Total depositado: R${total2-total}.00")

        char = input("APERTE ENTER PARA CONTINUAR")

    elif(indice == 2):
        if(total <= 0 ):
            print("SEM SALDO")
            char = input("APERTE ENTER PARA CONTINUAR")
            cofrinho(n100, n50, n20, n10, n5, n2, n1)

        print("Notas disponíveis no cofre:")
        relatorioSaque(n100, n50, n20, n10, n5, n2, n1)

        valor = int(input("Quanto deseja sacar? "))
        if(valor > total):
            option = input(f"O valor inserido não está disponível!\n Deseja sacar o salto total? R$ {total}.00 (y/n)")
            if(option=="y" or option=="Y"):
                print("Pegue seu dinheiro: ")
                n100, n50, n20, n10, n5, n2, n1 = sacar(n100, n50, n20, n10, n5, n2, n1, total)
                print(f"Valor sacado: R${total}.00")
                
        else:
            if( podeSacar(n100, n50, n20, n10, n5, n2, n1, valor)):
                print("Pegue seu dinheiro: ")
                n100, n50, n20, n10, n5, n2, n1 = sacar(n100, n50, n20, n10, n5, n2, n1, valor)
                print(f"Valor sacado: R${valor}.00")
            else:
                print("Não é possível sacar este valor!")
        char = input("APERTE ENTER PARA CONTINUAR")
    elif(indice==3):
        print(f"\nSeu saldo é de R${total}.00 ")
        char = input("APERTE ENTER PARA CONTINUAR")

    elif(indice == 4):
        print("RELATÓRIO")
        relatorio(n100, n50, n20, n10, n5, n2, n1)
        print(f"\nSeu saldo é de R${total}.00 ")
        char = input("APERTE ENTER PARA CONTINUAR")

    elif (indice == 0):
        if(total>0):
            print(f"Você ainda possui R${total}.00 ")
            option = input("Deseja sacar antes de fechar? (Y/N): ")
            if(option == "y" or option=="Y"):
                sacar(n100, n50, n20, n10, n5, n2, n1, total)
                print(f"Valor sacado: R${total}.00")
                
        char = input("APERTE ENTER PARA CONTINUAR")
        return

    cofrinho(n100, n50, n20, n10, n5, n2, n1)

cofrinho()
    
