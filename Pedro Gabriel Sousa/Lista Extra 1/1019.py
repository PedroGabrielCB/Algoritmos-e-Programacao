# URL do enunciado

# https://www.beecrowd.com.br/judge/pt/problems/view/1019

tempo = int(input())



horas = tempo / 3600

minutosResto = tempo % 3600

minutos = minutosResto / 60

segundos = minutosResto % 60



print("%.0f:%.0f:%.0f" %(horas,minutos,segundos))