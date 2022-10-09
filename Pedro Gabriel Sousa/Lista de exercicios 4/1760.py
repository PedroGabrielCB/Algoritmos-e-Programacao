# URL do enunciado

# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1760

contadorDePessoa = 1
contadorPeso = 0
SomaDeIdade = 0


while contadorDePessoa <= 4:
    contadorDePessoa = contadorDePessoa + 1
    idade = int(input())
    peso = float(input())

    
    SomaDeIdade = SomaDeIdade + idade
    
    if peso > 90:
        contadorPeso = contadorPeso + 1

    
media = SomaDeIdade / 4
print("Qtd pessoas > 90 Kg: %i" %(contadorPeso))
print("Idade média: %.2f" %(media))