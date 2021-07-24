# Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que
# calcule seu peso ideal, utilizando as seguintes fórmulas:
    # Para homens: (72.7*h) - 58
    # Para mulheres: (62.1*h) - 44.7


altura = input('Qual sua altura?')

if(len(altura) <= 0):
    print('Preciso saber sua altura')
    print('------------------------')
    print('Programa finalizado.')
    print('------------------------')
else:
    sexo = input("Você é homem ou mulher? ").upper()
    if(sexo==''):
        print('Preciso saber seu sexo.')
    else:

        if(sexo == 'HOMEM'):
            alt_float = float(altura)
            calc_homens = (72.7 * alt_float) - 58
            print(f'Como você é {sexo}, seu peso ideal é {calc_homens}')
        elif(sexo == 'MULHER'):
            alt_float = float(altura)
            calc_mulheres = (62.1 * alt_float) - 44.7
            print(f'Como você é {sexo}, seu peso ideal é {calc_mulheres}')
        elif(sexo!='HOMEM' or sexo != 'MULHER'):
            print('Você precisa informar se é HOMEM ou MULHER.')

print("FIM DO PROGRAMA")








