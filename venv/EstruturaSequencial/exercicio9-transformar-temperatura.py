#https://wiki.python.org.br/EstruturaSequencial
#Faça um Programa que peça a temperatura em graus Fahrenheit,
# transforme e mostre a temperatura em graus Celsius. C = 5 * ((F-32) / 9).

graus_far = float(input('Valor em Fahrenheit: '))
graus_celsius = 5 * ((graus_far-32)/9)
print(f'{graus_far} Fº equivale a {graus_celsius}ºC')
