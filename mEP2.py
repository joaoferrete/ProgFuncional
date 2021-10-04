x = float(input())
op = input()
y = float(input())

imprime = False

if y == 0 and (op == "//" or op == "%"):
    print("Divisao por 0!")

elif op == "+":
    resultado = x+y
    imprime = True
elif op == "-":
    resultado = x-y
    imprime = True
elif op == "*":
    resultado = x*y
    imprime = True
elif op == "**":
    resultado = x**y
    imprime = True
elif op == "//":
    resultado = x//y
    imprime = True
elif op =="%":
    resultado = x%y
    imprime = True

else:
    print("Operacao nao reconhecida!")

if imprime:
    print(f"{x} {op} {y} = {resultado}")
    