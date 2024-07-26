preco = float(input('Digite o preço do produto: R$ '))
desconto = preco - (preco * 5) / 100
print('O produto que custava R$ {:.2f}, aplicando o desconto de 5% o valor será de R$ {:.2f}' .format(preco, desconto))