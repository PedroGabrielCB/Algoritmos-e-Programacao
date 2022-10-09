tempo  = int(input()) 

velocidade = int(input())

distancia = velocidade * tempo 

LitrosPorKm = 1 / 12

consumo  = LitrosPorKm * distancia

print("%.3f" %(consumo))