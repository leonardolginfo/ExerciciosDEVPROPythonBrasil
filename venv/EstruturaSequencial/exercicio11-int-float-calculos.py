'''
Faça um Programa que peça 2 números inteiros e um número real. Calcule e mostre:

o produto do dobro do primeiro com metade do segundo .

a soma do triplo do primeiro com o terceiro.

o terceiro elevado ao cubo.
'''
num_1 = int(input('Digite o primeiro número: '))
num_2 = int(input('Digite o segundo número: '))
num_3 = float(input('Digite o terceiro número: '))

calculo_1 = (num_1**2) * (num_2/2)
print(f'O produto do dobro de {num_1} com metade de {num_2} é {calculo_1}')

calculo_2 = (num_1*3) + num_3
print(f'A soma do triplo de {num_1} com {num_3} é {calculo_2}')

calculo_3 = (num_3**3)
print(f'O triplo de {num_3} é {calculo_3}')