'''
3. Faça um programa que leia e valide as seguintes informações:
1. Nome: maior que 3 caracteres;
2. Idade: entre 0 e 150;
3. Salário: maior que zero;
4. Sexo: 'f' ou 'm';
5. Estado Civil: 's', 'c', 'v', 'd';
Obs: Deve ser criado uma função para cada item a ser verificado.
'''

def validar_nome():
    while True:
        nome = input("Digite seu nome: ").strip()
        if len(nome) > 3:
            return nome
        print("Erro: O nome deve ter mais de 3 caracteres.")

def validar_idade():
    while True:
        try:
            idade = int(input("Digite sua idade: "))
            if 0 <= idade <= 150:
                return idade
            print("Erro: A idade deve estar entre 0 e 150.")
        except ValueError:
            print("Erro: Digite um número inteiro válido.")

def validar_salario():
    while True:
        try:
            salario = float(input("Digite seu salário: "))
            if salario > 0:
                return salario
            print("Erro: O salário deve ser maior que zero.")
        except ValueError:
            print("Erro: Digite um valor numérico válido.")

def validar_sexo():
    while True:
        sexo = input("Digite seu sexo (f/m): ").strip().lower()
        if sexo in ['f', 'm']:
            return sexo
        print("Erro: O sexo deve ser 'f' ou 'm'.")

def validar_estado_civil():
    while True:
        estado_civil = input("Digite seu estado civil (s/c/v/d): ").strip().lower()
        if estado_civil in ['s', 'c', 'v', 'd']:
            return estado_civil
        print("Erro: Estado civil inválido. Use 's', 'c', 'v' ou 'd'.")

print("=================================================")
# Executando as funções. O programa só avança quando a função retorna um valor válido.
nome = validar_nome()
idade = validar_idade()
salario = validar_salario()
sexo = validar_sexo()
estado_civil = validar_estado_civil()

print("=================================================")
# Utilização de f-strings para formatação mais limpa
print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: R$ {salario:.2f}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estado_civil}")
print("=================================================")