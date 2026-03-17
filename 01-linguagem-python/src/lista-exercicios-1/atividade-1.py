'''
1.Tendo como dado de entrada a altura (h) de uma pessoa, construa um
algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
1. Para homens: (72.7*h) - 58
2. Para mulheres: (62.1*h) - 44.7
Obs: Construir funções independes: uma para homens e outra para
mulheres. O retorno decimal de cada função deve ser formatado em 2
casa decimais.
'''

def peso_ideal_homem(h):
    return round(((72.7*h) - 58), 2)

def peso_ideal_mulher(h):
    return round(((62.1*h) - 44.7), 2)

altura_mulher = 1.70
altura_homem = 1.70

print("=================================================")
print(f"O peso ideal para homem de {altura_homem:.2f}m é: {peso_ideal_homem(altura_homem):.2f} kg")
print(f"O peso ideal para mulher de {altura_mulher:.2f}m é: {peso_ideal_mulher(altura_mulher):.2f} kg")
print("=================================================")
