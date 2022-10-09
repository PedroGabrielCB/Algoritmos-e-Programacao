# URL do enunciado

# https://www.beecrowd.com.br/judge/pt/problems/view/1045

a = float(input())
b = float(input())
c = float(input())
x = 0


if (a < b):
    x = a;
    a = b
    b = x

if (b < c):
    x = b
    b = c
    c = x
    
if (a < b):
    x = a
    a = b
    b = x
    
if (a >= b + c):
    print("NAO FORMA TRIANGULO")
else:
  if (a * a == b * b + c * c):
     print("TRIANGULO RETANGULO")
  else:
    if (a * a > b * b + c * c):
        print("TRIANGULO OBTUSANGULO")
    else:
     if (a * a < b * b + c * c):
         print("TRIANGULO ACUTANGULO")
         
if a == b and b == c:
     print("TRIANGULO EQUILATERO")
else:
  if (a == b or b == c):
      print("TRIANGULO ISOSCELES")