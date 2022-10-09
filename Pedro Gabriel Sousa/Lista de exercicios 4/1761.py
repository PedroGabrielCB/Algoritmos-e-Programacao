# URL do enunciado

# https://www.beecrowd.com.br/judge/pt/custom-problems/view/1761

valorMercadoria = 1
valorTotaldaCompra = 0

while valorMercadoria != 0:
    valorMercadoria = float(input())
    valorTotaldaCompra = valorTotaldaCompra + valorMercadoria
    
    
valorpagocliente = float(input()) 
valortroco = valorpagocliente - valorTotaldaCompra 
print("Total da compra: R$%.2f" %(valorTotaldaCompra))
print("Valor pago: R$%.2f" %(valorpagocliente)) 
print("Troco: R$%.2f" %(valortroco))  