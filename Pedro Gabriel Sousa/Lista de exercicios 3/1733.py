# URL do enunciado

# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1733

nome = input()
horasExtras = float(input())
salarioMin = 1192.40
ValorHora = 10

SalarioHoraExtra = horasExtras * ValorHora
SalarioBruto = 3 * salarioMin + SalarioHoraExtra

if SalarioBruto > 2000:
    DescontoInss = 0.12 * SalarioBruto
else:
    DescontoInss = 0.5 * SalarioBruto
    

if SalarioBruto > 2000:
    DescontoImposto = 0.20 * SalarioBruto
else:
    DescontoImposto = SalarioBruto

SalarioLiq = SalarioBruto - DescontoImposto - DescontoInss

print("Nome: %s" %(nome))
print("Salário bruto: R$%.2f" %(SalarioBruto))
print("Salário líquido: R$%.2f" %(SalarioLiq))