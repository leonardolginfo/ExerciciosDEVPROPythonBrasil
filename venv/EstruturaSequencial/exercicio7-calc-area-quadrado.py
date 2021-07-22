#https://wiki.python.org.br/EstruturaSequencial
#Faça um Programa que calcule a área de um quadrado,
# em seguida mostre o dobro desta área para o usuário.

lado = float(input('Qual o valor do lado do quadrado? '))
area = lado**2
dobra_area = area**2
print(f'O quadrado tem {lado}, sua área é {area} e o dobro da área é {dobra_area}')