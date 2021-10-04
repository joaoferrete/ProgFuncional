def batata (q):
    """Função que indica o produto escolhido, mostra se está ou não no estoque e chama a função para pagamento"""
    if q>=1:# A variável q representa a quantidade de produtos    
        print("Você escolheu Batata DarkSide \nPreço:R$3,99\n")
        pagamento(3.99)
    else:
        print("Este produto está Indisponível no momento!\n")

def refrigerante (q):
    """Função que indica o produto escolhido, mostra se está ou não no estoque e chama a função para pagamento"""
    if q>=1: # q indica a quantidade de refrigerantes no estoque
        print("Você escolheu GuaraWan \nPreço: R$4,25\n")
        pagamento(4.25)
    else:
        print ("Este produto está Indisponível no momento!\n")

def chocolate(q):
    """Função que indica o produto escolhido, mostra se está ou não no estoque e chama a função para pagamento"""
    if q>=1: #q indica a quantidade de barras de chocolate disponíveis
        print("Você escolheu Chocolate Wayne \nPreço: R$5,98\n")
        pagamento(5.98)
    else:
        print("Este produto está Indisponível no momento!\n")

def suco(q):
    """Função que indica o produto escolhido, mostra se está ou não no estoque e chama a função para pagamento"""
    if q>=1:# Equivale a quantidade de produtos
        print("Você escolheu Suco MathaHato \nPreço: R$2,00\n")
        pagamento(2.00)
    else:
        print("Este produto está Indisponível no momento!\n")

def cha(q):
    """Função que indica o produto escolhido, mostra se está ou não no estoque e chama a função para pagamento"""
    if q>=1: #Mostra a quantidade de produtos disponíveis
        print("Você escolheu Chá Gelado Kenobi \nPreço: R$3,49\n")
        pagamento(3.49)
    else:
        print("Este produto está Indisponível no momento!\n")

def pagamento(n, w=0): # O parametro 'n' é o valor do produto, enquanto w é a soma dos valores inseridos pelo usuário
    """A função pagamento solicita a entrada de dinheiro até que a soma inserida seja igual ou maior que o valor do produto selecionado pelo usuário e, caso a quantidade inserida seja maior, chama a função para troco"""
    if w<n: #Será solicitado o dinheiro até que a soma seja maior que o valor
        receb=float(input("Coloque o dinheiro: "))
        pagamento(n, w+receb)
    else:
        g=round(w-n,2)#g é a variável responsável pela quantidade de troco a ser retornada ao usuário. Foi utilizada a função round para que não haja conflito ao retornar moedas de R$0,01
        if g==0: #Se g for igual a 0 não é necessário troco
            print("\nTroco: R$ {:.02f} \nOBRIGADO!\n".format(g))
        else:
            print("\nTroco: R$ {:.02f}\n".format(g))
            troco(g)#É chamada a função para que seja fornecido o troco

def troco(t): #t é o valor equivalente a g na função anterior, que representa a diferença entre o valor do produto e o valor inserid, ou seja, o troco   
    """Função que verifica o valor do troco e o imprime da forma que sejam devolvido da menor forma possível, e após imprime 'obrigado'""" 
    if t>0: #Se t>0 então existe troco a ser retornado
        if t>=100: #Se t maior que 100, então pode ser retornado uma nota de 100
            print ("R$ 100,00")
            troco(t-100) #Como já foi entregue uma nota de 100, então subtraí-se 100 do troco que precisa ser entregue
        elif t>=50: # O mesmo principio que a nota de 100 para todos os posteriores.
            print ("R$ 50.00") 
            troco(t-50)
        elif t>=20:
            print("R$ 20,00")
            troco(t-20)
        elif t>=10:
            print("R$ 10,00")
            troco(t-10)
        elif t>=5:
            print("R$ 5,00")
            troco(t-5)
        elif t>=2:
            print("R$ 2,00")
            troco(t-2)
        elif t>=1:
            print("R$ 1,00")
            troco(t-1)
        elif t>=0.50:
            print("R$ 0,50")
            troco(t-0.5)
        elif t>=0.25:
            print("R$ 0,25")
            troco(t-0.25)
        elif t>=0.10:
            print("R$ 0,10")
            troco(t-0.10)
        elif t>=0.05:
            print("R$ 0.05")
            troco(t-0.05)
        else:
            print("R$ 0.01")
            troco(round(t-0.01,2))
    else: #Se t for igual a zero, então todo o troco já foi entregue, então imprime-se 'Obrigado'
        print("\nOBRIGADO!\n")

def limpatela():
    """Função que limpa o terminal ao chamar a função principal 'maquina'"""
    from os import system, name  #Importa o que é necessário pra usar a função  
    if name=="nt":
        system("cls")
    else:
        system("clear")

def maquina(q=5,w=5,e=5,r=5,t=5): #q,w,e,r,t equivalem a quantidade de batatas, refrigerantes, chocolates, sucos e chás respectivamente   
    """Função principal do funcionamento da máquina, na qual imprime os produtos disponíveis e suas quantidades, verifica a escolha do usuário, chama a função do produto correspondente e após verifica se o usuário deseja efetuar outra compra"""
    if q==0 and w==0 and e==0 and r==0 and t==0: #Se todas as variáveis de quantidade forem iguais a zero, logo não existem produtos disponiveis para a compra
        print("\nDESCULPE, A MAQUINA ESTÁ SEM ESTOQUE!\n")
    else:
        limpatela() 
        print("\n -------------------------------------------------------------------------") #Menu de escolha do usuário   
        if q>0:
            print ("|  1- BATATA DARKSIDE                   -         PREÇO: R$3,99     Qt({}) |".format(q))
        else:
            print("|  1- BATATA DARKSIDE                   -         PRODUTO INDISPONÍVEL    |") #Se a variável responsável pela quantidade do produto for zero, é impresso que o produto está indisponível
        if w>0:
            print ("|  2- GUARAWAN                          -         PREÇO: R$4,25     Qt({}) |".format(w))
        else:
            print("|  2 -GUARAWAN                          -         PRODUTO INDISPONÍVEL    |")
        if e>0:
            print ("|  3- CHOCOLATE WAYNE                   -         PREÇO: R$5,98     Qt({}) |".format(e))
        else:
            print("|  3- CHOCOLATE WAYNE                   -         PRODUTO INDISPONÍVEL    |")
        if r>0:
            print ("|  4- SUCO MATHAHATO                    -         PREÇO: R$2,00     Qt({}) |".format(r))
        else:
            print("|  4- SUCO MATHAHATO                    -         PRODUTO INDISPONÍVEL    |")
        if t>0:
            print ("|  5- CHÁ GELADO KENOBI                 -         PREÇO: R$3,49     Qt({}) |".format(t))
        else:
            print("|  5- CHÁ GELADO KENOBI                 -         PRODUTO INDISPONÍVEL    |")
        print(" -------------------------------------------------------------------------")
        p=int(input("Escolha seu produto: "))#É solicitado ao usuário a escolha do produto a partir da numeração que o representa
        if p==1: #Se p for 1 o usuário escolheu a batata, então é chamada a função correspondente ao produto escolhido, no caso a batata, é passado o parametro de quantidade correspondende para a função do prooduto e ao fim da execução é perguntado se deseja efetuar uma nova compra
            batata(q)
            d=input("Deseja fazer outra compra? S/N: ")
            if d=="s" or d=="S": #Se o usuário desejar fazer uma nova compra, a função 'maquina' é chamada com o parametro do produto escolhido anteriormente subtraído uma unidade
                maquina(q-1,w,e,r,t)
            else: #Se o usuário não desejar efetuar outra compra é mostrado uma mensagem de 'volte sempre'
                print("\nVOLTE SEMPRE!")
        elif p==2:#O mesmo principio que o anterior também para os posteriores.
            refrigerante(w)
            d=input("Deseja fazer outra compra? S/N: ")
            if d=="s" or d=="S":
                maquina(q,w-1,e,r,t)
            else:
                print("\nVOLTE SEMPRE!")
        elif p==3:
            chocolate(e)
            d=input("Deseja fazer outra compra? S/N: ")
            if d=="s" or d=="S":
                maquina(q,w,e-1,r,t)
            else:
                print("\nVOLTE SEMPRE!")
        elif p==4:
            suco(r)
            d=input("Deseja fazer outra compra? S/N: ")
            if d=="s" or d=="S":
                maquina(q,w,e,r-1,t)
            else:
                print("\nVOLTE SEMPRE!")
        elif p==5:
            cha(t)
            d=input("Deseja fazer outra compra? S/N: ")
            if d=="s" or d=="S":
                maquina(q,w,e,r,t-1)
            else:
                print("\nVOLTE SEMPRE!")

maquina(5,5,5,5,5) #A função MAquina, que é a principal e que chama todas as outras, é chamada
