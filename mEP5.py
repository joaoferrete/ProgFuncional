def vI(entrada):
    if entrada =="x" or entrada == "o" or entrada == " ": return True
    else: return False

def ver(p1, p2, p3, p4, p5, p6, p7, p8, p9, simbolo):
    conta = 0
    if p1==simbolo: conta+=1
    if p2==simbolo: conta+=1
    if p3==simbolo: conta+=1
    if p4==simbolo: conta+=1
    if p5==simbolo: conta+=1
    if p6==simbolo: conta+=1
    if p7==simbolo: conta+=1
    if p8==simbolo: conta+=1
    if p9==simbolo: conta+=1

    return conta


def verifEspaco(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    if p1==" " or p2 == " " or p3 == " " or p4 == " " or p5 == " " or p6 == " " or p7 == " " or p8 == " " or p9 == " ":
        return True
    else:
        return False

def venceX(e1, e2, e3, e4, e5, e6, e7, e8, e9):
    if e1==e2==e3=="x": return True
    elif e1==e4==e7=="x": return True
    elif e1==e5==e9=="x": return True
    elif e2==e5==e8=="x": return True
    elif e3==e6==e9=="x": return True
    elif e3==e5==e7=="x": return True
    elif e4==e5==e6=="x": return True
    elif e7==e8==e9=="x": return True
    else: return False

def venceO(e1, e2, e3, e4, e5, e6, e7, e8, e9):
    if e1==e2==e3=="o": return True
    elif e1==e4==e7=="o": return True
    elif e1==e5==e9=="o": return True
    elif e2==e5==e8=="o": return True
    elif e3==e6==e9=="o": return True
    elif e3==e5==e7=="o": return True
    elif e4==e5==e6=="o": return True
    elif e7==e8==e9=="o": return True
    else: return False

def imprimeTabuleiro(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e imprime o tabuleiro
    """
    #Complete o código da função
    print(f" {p7} | {p8} | {p9} ")
    print("---+---+---")
    print(f" {p4} | {p5} | {p6} ")
    print("---+---+---")
    print(f" {p1} | {p2} | {p3} ")

def entradaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    verifica se os valores são válidos, ou seja, retorna True
    se cada variável possui " " ou "x" ou "o" e False, caso contrário.
    """
    #Complete o código da função
    if vI(p1) and vI(p2) and vI(p3) and vI(p4) and vI(p5) and vI(p6) and vI(p7) and vI(p8) and vI(p9):
        return True
    else:
        return False

def jogadaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    verifica se os valores formam uma jogada válida.

    Retorna True se a jogada for válida e False, caso contrário
    """
    #Complete o código da função
    if abs(ver(p1, p2, p3, p4, p5, p6, p7, p8, p9, "x" ) - ver(p1, p2, p3, p4, p5, p6, p7, p8, p9, "o"))>1:
        return False
    else: return True


def verificaJogada(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    imprime se um jogador ('x' ou 'o') venceu a jogada. 
    (Cada variável representa uma posição no tabuleiro)
    """
    #Complete o código da função
    if venceX(p1, p2, p3, p4, p5, p6, p7, p8, p9):
        print("O jogador 'x' venceu!")
    elif venceO(p1, p2, p3, p4, p5, p6, p7, p8, p9):
        print("O jogador 'o' venceu!")
    elif verifEspaco(p1, p2, p3, p4, p5, p6, p7, p8, p9):
        print("O jogo nao terminou!")
    else:
        print("Empate!")



## NÃO ALTERE A FUNÇÃO 'main' ##
def main():
    t1 = input()
    t2 = input()
    t3 = input()
    t4 = input()
    t5 = input()
    t6 = input()
    t7 = input()
    t8 = input()
    t9 = input()
    imprimeTabuleiro(t1, t2, t3, t4, t5, t6, t7, t8, t9)
    if not entradaValida(t1, t2, t3, t4, t5, t6, t7, t8, t9):
        print("Entrada invalida!")
    elif not jogadaValida(t1, t2, t3, t4, t5, t6, t7, t8, t9):
        print("Jogada invalida!")
    else:
        verificaJogada(t1, t2, t3, t4, t5, t6, t7, t8, t9)

main()
