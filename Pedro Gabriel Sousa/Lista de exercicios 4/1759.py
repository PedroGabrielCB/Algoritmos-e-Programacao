# URL do enunciado

# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1759

aumento = 0.015
salario = 1000
ano = 2005

entrada = int(input())

if entrada > ano: 
    while ano <= entrada:
            if ano == 2005:
                 ano = ano + 1
            elif ano == 2006:
                salario = salario + (salario * aumento)
                aumento = aumento + 0.01
                ano = ano + 1
            else:
                 salario = salario + (salario * aumento)
                 aumento = aumento + 0.01
                 ano = ano + 1
         
    print("Salário atual: R$%.2f" %(salario))
else:
    print("O ano informado deverá ser > 2005!")