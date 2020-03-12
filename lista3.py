
'''
#lista 3
#1

valorRecebido = int(input("digite um numero"))
if (valorRecebido<10):
    print("menor q 10")
else:
    print("maior q 10")

#2 Escrever um algoritmo que leia dois valores inteiro distintos e informe qual é o maior ou se
#houve um empate

valor1 = int(input("numero1"))
valor2 = int(input("numero2"))
if (valor1>valor2):
    print("numero 1 é maior")
else:
    print("numero 2 é maior")

#4
time1 = str(input("nome do time1"))
gols1 = int(input("qtd gols1"))
time2 = str(input("nome do time2"))
gols2 = int(input("qtd gols2"))

if (gols1>gols2):
    print(time1+" é o vencedor")
elif (gols2>gols1):
    print(time2+" é o vencedor")
else:
    print("EMPATE")


#5
jornadaExigida = int(input("qual a jornada"))

jornada = int(8)
diasTrabalhados = int(input("qts dias trabalhou?"))
horasTrabalhadas = int(jornada*diasTrabalhados)
print(horasTrabalhadas)

valorHora = float(input("qual o valor da hora regular?"))
valorHoraExtra = float(valorHora*1.5)
print("Valor Hora Extra: "+str(valorHoraExtra))

salarioRegular = int(valorHora*horasTrabalhadas)
print("Valor do Salario do mes: "+str(salarioRegular))

horasAdicionais = int(horasTrabalhadas-jornadaExigida)
valorExtraPagar = float(valorHoraExtra*horasAdicionais)


if(horasAdicionais>0):
    print("qtd horas adicionais: "+str(horasAdicionais))
    print("Valor Extra a Pagar: "+str(valorExtraPagar))
else:
    print("sem hora extra")

salarioTotal = int(salarioRegular+valorExtraPagar)
print(salarioTotal)
#6 Faça um programa para ler dois números inteiros A e B e informar se A é divisível por B
numA = int(input("digite o num A"))
numB = int(input("digite o num B"))


temResto = int(numA % numB)
if(temResto == 0):
    print("divisivel")
elif(temResto !=0):
    print("teve resto, nao divisivel")

#7
num = int(input("digite um numero"))
raiz = float(math.sqrt(num))
print(raiz)

#8 Escreva um algoritmo que recebe a idade de um nadador e mostra sua categoria conforme a
idade = int(input("Digite a idade do nadador"))
if(idade>30):
    print("Senior")
elif(idade>=16):
    print("Adulto")
elif(idade>=11):
    print("Adolescente")
elif(idade>=8):
    print("Juvenil")
elif(idade>=5):
    print("Infantil")
else:
    print("abaixo de 5")

#9
dividendo = int(input("numero do dividendo"))
divisor = int(input("digite o divisor"))
if(divisor==0):
    print("não é possivel fazer contas com divisor ZERO")
else:
    resultado = int(dividendo / divisor)
    print(resultado)

#10
import math
a = int(input("digite o valor de A"))
b = int(input("digite o valor de B"))
c = int(input("digite o valor de C"))
print("A formula ficou assim: " + str(a)+"x**2 +"+str(b)+"x + "+str(c)+" = 0")

delta = float(b*b - (4*a*c))
print(delta)
if(delta<0):
    print("delta negativo")
else:
    x1 = float((-b + math.sqrt(delta)) / 2*a)
    print(x1)
    x2 = float((-b - math.sqrt(delta)) / 2*a)
    print(x2)

#11
precoEtiqueta = int(input("qual preco de etiqueta?"))
condicaoPagto = int(input("QUal a condicao: 1 , 2 , 3 , 4"))
if(condicaoPagto==1):
    print("recebe 10%")
    valorPagar = int(precoEtiqueta*0.9)
    print("Valor a pagar: "+str(valorPagar))
elif(condicaoPagto==2):
    print("recebe 5%")
    valorPagar = int(precoEtiqueta*0.95)
    print("Valor a pagar: "+str(valorPagar))
elif(condicaoPagto==3):
    print("em 2 vezes, preco regular")
    valorPagar = int(precoEtiqueta*1)
    print("Valor a pagar: "+str(valorPagar))
elif(condicaoPagto==4):
    print("em 4 vezes tem 7% de juros")
    valorPagar = int(precoEtiqueta*1.07)
    print("Valor a pagar: "+str(valorPagar))
else:
    print("numero invalido")
'''
#12


