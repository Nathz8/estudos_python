salario = float(input('Qual o salário do funcionário? R$'))
aumento = salario + (salario * 15) / 100
print('O salário do funcionário atualmente é R$ {:.2f}, com um aumento de 15% o salário será R$ {:.2f}' .format(salario, aumento))