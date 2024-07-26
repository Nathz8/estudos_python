#Faça um programa que leia algo pelo teclado e motre na tela o seu tipo primitivo e todas as informações possiveis sobre ele.
leitor = input ('Digite algo: ')
print ('O tipo primitivo desse valor é {}' .format(type(leitor)))
print ('Possui espaço? {}' .format(leitor.isspace()))
print ('É um número? {}' .format(leitor.isnumeric()))
print ('Possui letras? {}' .format(leitor.isalpha()))
print ('É alfanumérico? {}' .format(leitor.isalnum()))
print ('Está maiúscula? {}' .format(leitor.isupper()))
print ('Está minúscula? {}' .format(leitor.islower()))
print ('Está capitalizada? {}' .format(leitor.istitle()))
#Mesmo script, utilizando um só: print('  {}'.format())
leitor = input ('Digite ao algo: ')     
print ('O tipo primitivo desse valor é: {0}.\n Possui espaços? {1}.\n É um número? {2}.\n É uma letra? {3}.\n Possui letras e números? {4}.\n Letras maiusculas? {5}.\n Letras minusculas? {6}.\n Está capitalizada? {7}' 
       .format(type(leitor), 
               leitor.isspace(),
               leitor.isnumeric(),
               leitor.isalpha(),
               leitor.isalnum(),
               leitor.isupper(),
               leitor.islower(),
               leitor.istitle()))