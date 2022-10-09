# URL do enunciado

# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1716

cod = input()
ValorTotal = float(input())


if cod.upper() == "A":
    Total = ValorTotal + (ValorTotal * 0.10)
elif cod.upper() == "B":
    Total = ValorTotal + (ValorTotal * 0.15)
elif cod.upper() == "C":
    Total = ValorTotal + (ValorTotal * 0.20)
else:
    Total = 0

if Total != 0:
    print("Novo salário: R$%.2f" %(Total))
else:
    print("OPÇÃO INVÁLIDA!")