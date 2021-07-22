#Faça um Programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.
#F = C x 1,8 + 32

temp_celsius = float(input('Temperatura em ºC:'))
temp_f = (temp_celsius*1.8) + 32
print(f'A temperatura {temp_celsius}ºC equivale a {temp_f}ºF')