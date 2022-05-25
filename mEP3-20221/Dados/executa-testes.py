import os
import sys


def executaTestes(mEParq, i = 1, tempoLimite = 2):
    arqTeste = "arq" + str(i) +".in"
    if not os.path.exists(arqTeste):
        return

    arqResp  = "arq" + str(i) +".sol"
    if not os.path.exists(arqResp) :
      print("Arquivo {} não encontrado.".format(arqResp))
      exit()

    outfile = "arq" + str(i) +".out"
    if (os.path.exists(outfile)) :
       resp = input("Arquivo " + outfile + " existente. Pode ser sobrescrito (S/n) ?")
       if resp == "n" or resp == "N" :
         exit()

    difffile = "arq" + str(i) +".diff"
    if (os.path.exists(difffile)) :
       answer = input("Arquivo " + difffile + " existente. Pode ser sobrescrito (S/n) ?")
       if answer == "n" or answer == "N" :
         sys.exit()

    os.system("python3 " + mEParq + " < " + arqTeste + " > " + outfile)
    if os.system("diff " + outfile + " " + arqResp + " > " + difffile) == 0 :
       print("Teste {}: resultado correto".format(i))
    else: 
       print("Teste {}: resultado incorreto".format(i))
       # os.system("cat " + difffile)
    os.remove(outfile)      
    os.remove(difffile)
    executaTestes(mEParq, i + 1, tempoLimite)

def main():
    if len(sys.argv) < 2 :
        print("Uso: python3 executa-testes.py mEPXX.py")
        exit()

    mEParq = sys.argv[1]
    if not os.path.exists(mEParq) :
        print("Arquivo {} não encontrado.".format(mEParq))
        exit()
    executaTestes(mEParq)

main()