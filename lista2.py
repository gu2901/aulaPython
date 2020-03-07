#2
print("exercicio 2:")
nome = input("seu nome")
sobrenome = input("seu sobrenome")

print(sobrenome)
print(nome)

#3

print("exercicio 3:")
nomePessoa = input("diga seu nome: ")
anoNascimento = int(input(nomePessoa+" em que ano voce nasceu?"))

anoAtual = 2020
idade = int(anoAtual - anoNascimento)
print(idade)
print(str(anoNascimento)+", uau, isso quer dizer que em 2020 você terá: "+str(idade))

#4
print("exercicio 4:")
numero1 = int(input("escolha um numero"))
numero2 = int(input("escolha outro numero"))

soma = numero1 + numero2
multiplica = numero1 * numero2
divide = int(numero1 / numero2)
resto = numero1 % numero2

print(soma,multiplica,divide,resto)

#5
print("exercicio 5:")
num1 = int(input("escolha X"))
num2 = int(input("escolha Y"))
potencia = num1**num2
print(potencia)


#6
print("exercicio 6:")
diametro = float(input("qual o diametro do circulo?"))
raio = float(diametro/2)
area = float(3.141592 * (raio*raio))
perimetro = float(2 * 3.141592 * raio)
print("a area é:"+str(area))
print("o Perimetro  é:"+str(perimetro))

#7
print("exercicio 7:")
numRecebido = int(input("escolha um numero de 0 a 99"))
numeroMalandro = float(numRecebido/10)
arrayEsperto = [str(numeroMalandro)]

print(numeroMalandro)
print(arrayEsperto)

#8.
print("exercicio 8:")
qtdCamisa = int(input("vc tem qts camisas?"))
if qtdCamisa > 10:
    print("caramba, quanta camisa")
qtdCalca = int(input("vc tem qts calcas?"))
paresSapato =int(input("vc tem qts sapatos?"))

print(qtdCamisa*qtdCalca*paresSapato)


#9
print("exercicio 9:")
preco = int(input("qual o preço do produto?"))
percentual = int(input("qual o desconto?"))

valorDesconto = preco*percentual/100
novoPreco = preco-valorDesconto
aumento = preco+valorDesconto

print(valorDesconto)
print(novoPreco)
print(aumento)


#10
print("exercicio 10:")
from decimal import Decimal
distPercorrida = 100
tempo = 9.58

velKmh = round(Decimal((distPercorrida/1000)/(tempo/60)),2)
velMss = round(Decimal(distPercorrida/tempo),2)

print(str(velMss)+"m/s")
print(str(velKmh)+"km/h")


#11
print("exercicio 11:")
salarioAntigo = float(input("Antigo Salario"))
salarioNovo = float(input("Novo Salario"))

percentual = int((salarioNovo/salarioAntigo-1)*100)
print(str(percentual)+"% de aumento")

#12
print("exercicio 12.1:")

#metodo1
rmRecebido = input("informe o RM")
arrayApoio = []
if len(rmRecebido)<5:
    print("o rm deve ter 5 numeros")
for numeros in rmRecebido:
    arrayApoio.append(numeros)
print(arrayApoio)
soma = 0
for numeros in arrayApoio:
    soma = int(numeros)+soma
print(soma)
#metodo2
print("exercicio 12.2:")
primeiro = int(int(rmRecebido)/10000)
restoPrimeiro = int(int(rmRecebido)%10000)
segundo = int(int(restoPrimeiro)/1000)
restoSegundo = int(int(restoPrimeiro)%1000)
print(segundo)
print(restoSegundo)

#13
print("exercicio 13:")
pesoNAC = 2
pesoAM = 3
pesoPS = 5

notaNAC = int(input("nota NAC"))
notaAM = int(input("nota AM"))
notaPS = int(input("nota PS"))

media = (notaNAC*pesoNAC + notaAM*pesoAM + notaPS*pesoPS)/10
print(media)

#14
print("exercicio 14:")
valorVista = int(input("qual o valor a Vista?"))
valorParcelado = int(input("qual o valor a Parcelado?"))
valorParceladoSomado = valorParcelado*10
print(valorParceladoSomado)

descontoConcedido = 100 - int(valorVista/valorParceladoSomado*100)
print("Desconto concedido de "+ str(descontoConcedido)+"%")