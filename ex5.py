num = soma = cont = 0
while True:
    num = int(input('Digite um numero [999 para finalizar]:\n'))
    if num != 999:
        soma += num
        cont += 1
    else:
        break
print('Foram digitados ao todo {} numeros e a soma dos valores é {} '.format(cont,soma))
