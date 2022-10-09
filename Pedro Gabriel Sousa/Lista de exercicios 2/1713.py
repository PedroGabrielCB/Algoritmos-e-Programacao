# URL do enunciado

# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1713

ganhoPorhora = float(input())
numPorMes = float(input())


salarioTotal = ganhoPorhora * numPorMes
Imposto = salarioTotal * 0.11
INSS = salarioTotal * 0.08
Sindicato = salarioTotal * 0.05
Liquido = salarioTotal - Imposto - INSS - Sindicato 

print("Salário bruto: R$%.2f\nImposto: R$%.2f\nINSS: R$%.2f\nSindicato: R$%.2f\nLíquido: R$%.2f\n" %(salarioTotal,Imposto,INSS,Sindicato,Liquido))
