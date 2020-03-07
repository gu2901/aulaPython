#Esgotamento

#Iniciar perguntando quantos elementos vai ter nosso array
qtdNumerosNoArray = int(input("quantos numeros terá o array?"))

arrayComMeusNumeros = []
i = 0

while i < qtdNumerosNoArray:
    numeroAdicionado = int(input("Qual o valor do numero" + str(i+1)))
    arrayComMeusNumeros.append(numeroAdicionado)
    i+= 1

print(arrayComMeusNumeros)
#numeros incluidos, agora vamos sortear por ESGOTAMENTO

loop = 0

for x in arrayComMeusNumeros:
    proximoNum = loop +1
    print(arrayComMeusNumeros[loop])
    if arrayComMeusNumeros[loop] > arrayComMeusNumeros[proximoNum]:
        print("Encontrou Num Menor: "+str(arrayComMeusNumeros[proximoNum]))
        loop +=1
        print("qtd loops: "+str(loop))
        arrayComMeusNumeros[loop]= arrayComMeusNumeros[proximoNum]
    print("fim do if")
print("fim do for")    

    #   menorNumero = arrayComMeusNumeros[1]

    
