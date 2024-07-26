numero = int(input('Informe um número: '))
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2)
print ('O dobro do valor é {}, \n o triplo do valor é {}, \n a raiz do valor é {}' .format(dobro, triplo, raiz))

#Outra forma
numero = int(input('Informe um número: '))
print ('O dobro do valor é {}, \n o triplo do valor é {}, \n a raiz do valor é {:.2f}' .format((numero * 2), (numero * 3), (numero ** (1/2))))