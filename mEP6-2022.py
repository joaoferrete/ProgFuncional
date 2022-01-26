def diminui(n , p):
    return 0 if n - p/2 <= 0 else n-p/2

def idPar(t, ar, f, ag, p, ent):
    if ent == "TERRA":
        ar = diminui(ar, p)
        t += p
    elif ent == "AR":
        t = diminui(t, p)
        ar += p
    elif ent == "AGUA":
        f = diminui(f, p)
        ag += p
    elif ent == "FOGO":
        ag = diminui(ag, p)
        f += p
    return ar, t, f, ag

def entra(t, ar, f, ag):
    ent = input()
    if ent == "FIM":
        return t, ar, f, ag
    p = int(input())
    ar, t, f, ag = idPar(t, ar, f, ag, p, ent)
    return entra(t, ar, f, ag)

def main():
    t, ar, f, ag = entra(0, 0, 0, 0)
    print("Pontuacao Final")
    print(f"Agua: {ag:.01f}")
    print(f"Terra: {t:.01f}")
    print(f"Fogo: {f:.01f}")
    print(f"Ar: {ar:.01f}")
    if(ag > 0 and t > 0 and f > 0 and ar > 0):
        print("Treinamento realizado com sucesso.")
    else:
        print("Realize mais treinamentos.")

main()
