from os import system , name
def limpaTela ():
    if name == 'nt':
        system ('cls ')
    else:
        system ('clear ')

def menu():
    print("\n\n1 - Café Puro - R$ 3.50")
    print("2 - Café com Leite - R$ 4.50")
    print("3 - Café com Açucar - R$ 5.50")
    print("4 - Café com Leite e Açucar - R$ 6.50")
    print("----------------------------------------")
    print("5 - Informações de Produtos")
    print("6 - Informações de Estoque")
    print("7 - Faturamento")
    print("0 - Sair\n\n")

def informacoesE(cafe, leite, agua, acucar):
    print(f"\nCafé: {cafe}g.")
    print(f"Leite: {leite}g.")
    print(f"Água: {agua}ml.")
    print(f"Açúcar: {acucar}g.")

def informacoesP():
    print("\n\nCafé Puro: 15g Café, 50ml Água, 1 Copo")
    print("\nCafé com Leite: 15g Café, 50ml Água, 30g Leite, 1 Copo")
    print("\nCafé com Açúcar: 15g Café, 50ml Água, 20g Açúcar, 1 Copo")
    print("\nCafé com Leite e Açúcar: 15g Café, 50ml Água, 30g Leite, 20g Açúcar, 1 Copo\n")


def troco(valor):
    if valor <= 0: return
    if valor >= 100:
        print("R$ 100.00")
        troco(valor - 100)
    elif valor >= 50:
        print("R$ 50.00")
        troco(valor - 50)
    elif valor >= 20:
        print("R$ 20.00")
        troco(valor - 20)
    elif valor >= 10:
        print("R$ 10.00")
        troco(valor - 10)
    elif valor >= 5:
        print("R$ 5.00")
        troco(valor - 5)
    elif valor >= 2:
        print("R$ 2.00")
        troco(valor - 2)
    elif valor >= 1:
        print("R$ 1.00")
        troco(valor - 1)
    elif valor >= 0.5:
        print("R$ 0.50")
        troco(valor - 0.5)
    elif valor >= 0.25:
        print("R$ 0.25")
        troco(valor - 0.25)
    elif valor >= 0.10:
        print("R$ 0.10")
        troco(valor - 0.10)
    elif valor >= 0.05:
        print("R$ 0.05")
        troco(valor - 0.05)
    elif valor >= 0.01:
        print("R$ 0.01")
        troco(valor - 0.01)
    else:
        print("R$ 0.01")
        troco(valor - 0.01)


def dinheiro(valor, totalEntrada=0):
    ent = float(input("\nInsira o dinheiro: R$ "))
    totalEntrada += ent
    if(valor == totalEntrada):
        print("Obrigado pela compra!\nRetire seu produto.")
    elif(valor > totalEntrada):
        dinheiro(valor, totalEntrada)
    else:
        print("\nRetire seu troco:")
        troco(totalEntrada - valor)
        print("\nObrigado pela compra!\nRetire seu produto.\n\n")
        input("Aperte ENTER para continuar.")

def coffee(fat = 0, copo=15, cafe = 100, leite = 200, agua = 1000, acucar = 250):
    limpaTela()
    menu()
    op = int(input("Digite a opção desejada: "))
    if op == 1:
        if copo > 0 and cafe >= 15 and agua >= 50:
            print("\nProduto Escolhido: Café Puro\nValor: R$ 3.50")
            dinheiro(3.50)
            copo -= 1
            cafe -= 15
            agua -= 50
            fat+=3.5
        else:
            print("\nEste produto está temporariamente indisponível")
            input("Aperte ENTER para continuar.")
            
    elif op == 2:
        if copo > 0 and cafe >= 15 and leite >= 30 and agua >= 50:
            print("\nProduto Escolhido: Café com Leite\nValor: R$ 4.50")
            dinheiro(4.50)
            copo -= 1
            cafe -= 15
            leite -= 50
            agua -= 50
            fat+=4.5
        else:
            print("\nEste produto está temporariamente indisponível")
            input("Aperte ENTER para continuar.")
    elif op == 3:
        if copo > 0 and cafe > 15 and agua >= 50 and acucar >= 20:
            print("\nProduto Escolhido: Café com Açucar\nValor: R$ 5.50")
            dinheiro(5.50)
            copo -= 1
            cafe -= 15
            agua -= 50
            acucar -= 20
            fat+=5.5
        else:
            print("\nEste produto está temporariamente indisponível")
            input("Aperte ENTER para continuar.")
    elif op == 4:
        if copo > 0 and cafe > 15 and leite >= 30 and agua >= 50 and acucar >= 20:
            print("\nProduto Escolhido: Café com Leite e Açucar\nValor: R$ 6.50")
            dinheiro(6.50)
            copo -= 1
            cafe -= 15
            leite -= 50
            agua -= 50
            acucar -= 20
            fat+=6.5
        else:
            print("\nEste produto está temporariamente indisponível")
            input("Aperte ENTER para continuar.")
    elif op == 5:
        informacoesP()
        input("\nAperte ENTER para continuar.")

    elif op == 6:
        informacoesE(cafe, leite, agua, acucar)
        input("\nAperte ENTER para continuar.")
    elif op == 7:
        print(f"O faturamento é de R${fat:.02f}")
        input("\nAperte ENTER para continuar.")
    elif op == 0: return

    coffee(fat, copo, cafe, leite, agua, acucar)

coffee()
