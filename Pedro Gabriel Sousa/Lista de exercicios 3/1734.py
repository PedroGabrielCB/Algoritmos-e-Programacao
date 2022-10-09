# URL do enunciado

# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1734

num = int(input())

resultado=1
count=1

while count <= num:
    resultado = resultado * count
    count = count + 1

print("%i! = %i" %(num,resultado))