#https://wiki.python.org.br/EstruturaSequencial
#Faça um Programa que peça as 4 notas bimestrais e mostre a média.

nota1 = int(input("Digite a nota do 1º bimestre: "))
nota2 = int(input("Digite a nota do 2º bimestre: "))
nota3 = int(input("Digite a nota do 5º bimestre: "))
nota4 = int(input("Digite a nota do 4º bimestre: "))

media = (nota1+nota2+nota3+nota4)/4
print(f'A média é: {media}')