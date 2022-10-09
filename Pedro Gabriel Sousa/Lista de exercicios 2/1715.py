# URL do enunciado

# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1715

cod = int(input())
ValorTotal = float(input())


if cod == 1:
    Total = ValorTotal
elif cod == 2:
    Total = ValorTotal - (ValorTotal * 0.13)
elif cod == 3:
    Total = ValorTotal - (ValorTotal * 0.07)
else:
    Total = 0

if Total != 0:
    print("Valor total a ser pago: R$%.2f" %(Total))
else:
    print("OPÇÃO INVÁLIDA!")