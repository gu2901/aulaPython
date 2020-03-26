#1
arraydeNumerosRecebidos = input("Digite a sequencia de numeros")
for numeros in arraydeNumerosRecebidos:
    if (int(numeros)%2 == 0):
        print(numeros)

#2
qtdAlunos = int(input("Digite a quantidade de alunos"))
arrayNotas = []

i=1
while(qtdAlunos >= i):
    notadoAluno = int(input("Digite a nota do aluno"+str(i)))
    arrayNotas.append(notadoAluno)
    print(arrayNotas)
    i=i+1

soma = sum(arrayNotas)
print(soma)
qtd = len(arrayNotas)
print(qtd)

avg = soma/qtd
print(avg)