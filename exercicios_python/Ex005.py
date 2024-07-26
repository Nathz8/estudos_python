numero = int(input('Informe um número: '))
antecessor = numero - 1
sucessor = numero + 1
print (f'Analisando o número {numero}, seu antecessor é {antecessor} e o seu sucessor é {sucessor}')
#outra forma
numero = int(input('Informe um número: '))
print ('Analisando o número {}, seu antecessor é {} e o seu sucessor é {}' .format(numero, (numero-1), (numero+1)))