#https://wiki.python.org.br/EstruturaSequencial
#Faça um Programa que pergunte quanto você ganha
# por hora e o número de horas trabalhadas no mês.
# Calcule e mostre o total do seu salário no referido mês.

valor_hora = float(input('Qual o valor da sua hora trabalhada? '))
horas_trabalhadas = int(input('Quantas horas você trabalhou? '))
salario = valor_hora * horas_trabalhadas
print(f'''Você trabalhou: {horas_trabalhadas}
Seu salário é de: R${salario}''')