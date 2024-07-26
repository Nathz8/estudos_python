largura = float(input('Informe a largura da parede em metros: '))
altura = float(input('Informe a altura da parede em metros: '))
metro_quadrado = 2
area = largura * altura
tinta = area / metro_quadrado
print ('Sua parede tem a dimenção de {:.2f} x {:.2f} e sua área é de {:.2f}m² \n Serão utilizados {:.2f}l de tinta' .format(largura, altura, area, tinta))