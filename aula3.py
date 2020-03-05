#encontre o X:  x**2 + 3x − 10 = 0
'''
import math 
delta = (3**2)-(4*10*1)
print(delta)


print(math.sqrt(36))  
x1 = float(-3) + float(math.sqrt(delta)) / 2

x2 = (-3 - float(math.sqrt(delta)))/2

print(x1)
print(x2)
'''

#encontre o maior numero

arrayDeNumeros = []
num1 = int(input("Digite o Numero 1"))
num2 = int(input("Digite o Numero 2"))
num3 = int(input("Digite o Numero 3"))
num4 = int(input("Digite o Numero 4"))
num5 = int(input("Digite o Numero 5"))


arrayDeNumeros.append(num1)
arrayDeNumeros.append(num2)
arrayDeNumeros.append(num3)
arrayDeNumeros.append(num4)
arrayDeNumeros.append(num5)

print(arrayDeNumeros)

print(max(arrayDeNumeros))

maior = 0
for x in arrayDeNumeros:
    if int(x) > maior:
        maior = int(x)
print(maior)

soma = 0
for x in arrayDeNumeros:
    print(x)
    soma =+ soma + int(x)
print(soma)


#problema 2.2
base = int(input("Tamanho da BASE do Triangulo: "))
altura = int(input("Tamanho da ALTURA do Triangulo: "))
area = base*altura/2
print(area)