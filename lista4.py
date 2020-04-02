'''
#1
arraydeNumerosRecebidos = str(input("Digite a sequencia de numeros"))
i=0
soma = 0
tam = len(arraydeNumerosRecebidos)
while (i<tam):
    if(i%2==0):
        numVez = arraydeNumerosRecebidos[i]
        print(numVez)
        soma = int(numVez) + soma
    i = i+1
print(soma)



#2 e 3
qtdAlunos = int(input("Digite a quantidade de alunos"))
arrayNotas = []
i=1
acima5 = []
ate5 = []

while(qtdAlunos >= i):
    notadoAluno = int(input("Digite a nota do aluno"+str(i)))
    if(notadoAluno>=5):
        acima5.append(int(notadoAluno))
    else:
        ate5.append(int(notadoAluno))
    arrayNotas.append(notadoAluno)
    i=i+1

print(arrayNotas)

soma = sum(arrayNotas)
print(soma)
qtd = len(arrayNotas)
print(qtd)
avg = soma/qtd
print(avg)

print(acima5)
print(ate5)

#4
numsPositivos = []
numsNegativos = []
n = int(input("Digite a quantidade de numeros"))
i=1
while i<= n:
    numDaVez = int(input("Digite o numero da vez"))
    if numDaVez>0:
        numsPositivos.append(numDaVez)
    else:
        numsNegativos.append(numDaVez)
    i+=1
print(numsPositivos)
print(numsNegativos)

#5
numDaVez = int(input("Digite o numero da vez"))
divisor = 2
while numDaVez >= divisor:
    if numDaVez % divisor == 0:
        print("Divisor de "+str(divisor))
    divisor+=2

#6
import random
totalCandidatos = 20
notas =[]
i=0

while i < totalCandidatos:
    aleatorio = random.randint(0,70)
    notas.append(aleatorio)
    i+=1
print(notas)

menorNota = max(notas)
print(menorNota)
maiorNota = min(notas)
print(maiorNota)
i = 0

acertouAte20 = 0
acertouDe21a50 = 0
acertouAcima50 = 0

while i < len(notas):
    if notas[i]<20:
        acertouAte20+=1
    elif notas[i]<50:
        acertouDe21a50+=1
    else:
        acertouAcima50+=1
    i+=1

porcAte20 = float(acertouAte20/totalCandidatos)
porc20a50 = float(acertouDe21a50/totalCandidatos)
porcAcima50 = float(acertouAcima50/totalCandidatos)
print(porcAte20)
print(porc20a50)
print(porcAcima50)

'''
#7
grausFarInic = 50
grausFarFim = 150

while grausFarInic < grausFarFim:
    celcius = 5/9*(grausFarInic-32)
    print(grausFarInic,celcius)
    grausFarInic+=1

#8
