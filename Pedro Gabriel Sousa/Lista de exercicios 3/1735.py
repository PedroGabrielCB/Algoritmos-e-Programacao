# URL do enunciado

# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1735

numFinal = int(input())
numInicial = int(input())

contador = numFinal

while numFinal >= numInicial:
    print(contador)
    contador = numFinal - 1
    numFinal =  numFinal - 1
    

print("Fogo!")