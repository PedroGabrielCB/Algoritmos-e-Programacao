# URL do enunciado

# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1714

PrecoProduto = float(input())


if PrecoProduto < 20:
    Total = PrecoProduto + (PrecoProduto * 0.45)
else:
    Total = PrecoProduto + (PrecoProduto * 0.30)
    

print("Valor de venda: R$%.2f" %(Total))