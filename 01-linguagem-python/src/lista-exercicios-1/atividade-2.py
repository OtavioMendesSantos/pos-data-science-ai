'''
2. Faça um Programa que peça a temperatura em graus Fahrenheit,
transforme e mostre a temperatura em graus Celsius.
C = 5 * ((F-32) / 9).
Obs: Deve-se realiza um tratamento, onde o valor em Fahrenheit não
deve ser negativo
'''

def fahrenheit_para_celsius(fahrenheit):
    if fahrenheit < 0:
        raise ValueError("O valor em Fahrenheit não deve ser negativo.")
    
    celsius = 5 * ((fahrenheit - 32) / 9)
    return round(celsius, 2)

try:
    fahrenheit_input = float(input("Digite a temperatura em Fahrenheit: "))
    celsius_output = fahrenheit_para_celsius(fahrenheit_input) 

    print("=================================================")
    print(f"A temperatura em Celsius é: {celsius_output}")
    print("=================================================")

except ValueError as erro:
    print(f"Erro de validação: {erro}")