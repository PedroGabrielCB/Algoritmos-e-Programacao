valor = float(input())

notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]

print('NOTAS:')
for nota in notas:
    qt_notas = int(valor / nota)
    print("%i nota(s) de R$ %i" %(qt_notas,nota))
    valor = valor - qt_notas * nota
print('MOEDAS:')
for moeda in moedas:
    qt_moedas = int(valor / moeda)
    print("%i moeda(s) de R$ %.2f" %(qt_moedas,moeda))
    valor = valor - qt_moedas * moeda
