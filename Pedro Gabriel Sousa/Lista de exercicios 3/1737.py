# URL do enunciado

# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1737

qtdNum = int(input())

contador = 1
resultado = 0


if qtdNum > 0:
    while qtdNum >= contador:
        num = float(input())
        resultado = resultado + num
        qtdNum = qtdNum - 1
        
    print("Soma dos números informados: %.2f" %(resultado))
else:   
    print("Informe uma quantidade > 0!")
    