# ==========================================
# TIPOS DE DADOS NATIVOS EM PYTHON (BUILT-IN)
# ==========================================

# 1. Tipos Numéricos (Numeric Types)
tipo_inteiro = 10          # int: Números inteiros (positivos ou negativos, sem decimais)
tipo_flutuante = 3.14      # float: Números decimais (ponto flutuante)
tipo_complexo = 2 + 3j     # complex: Números complexos (parte real + parte imaginária)

# 2. Tipo de Texto (Text Type)
tipo_texto = "Data Science" # str: Cadeia de caracteres (string). Pode usar aspas simples ou duplas.

# 3. Tipo Booleano (Boolean Type)
tipo_booleano = True       # bool: Valores lógicos (True ou False). Sensível a maiúsculas.

# 4. Tipos de Sequência (Sequence Types)
tipo_lista = [1, 2, 3]     # list: Sequência ordenada e mutável (permite alteração).
tipo_tupla = (1, 2, 3)     # tuple: Sequência ordenada e imutável (não permite alteração após criada).
tipo_range = range(0, 10)  # range: Sequência imutável de números, muito usada em laços (loops).

# 5. Tipo de Mapeamento (Mapping Type)
tipo_dicionario = {"id": 1, "nome": "IA"} # dict: Coleção não ordenada de pares chave:valor. Mutável.

# 6. Tipos de Conjunto (Set Types)
tipo_set = {1, 2, 3}       # set: Coleção não ordenada de elementos únicos. Mutável e não indexada.
tipo_frozenset = frozenset({1, 2, 3}) # frozenset: Versão imutável do set.

# 7. Tipo Nulo (None Type)
tipo_nulo = None           # NoneType: Representa a ausência de valor ou um valor nulo.

# ==========================================
# EXIBINDO OS TIPOS NO TERMINAL
# ==========================================
# A função type() retorna a classe do objeto.
print(type(tipo_inteiro))    # Saída: <class 'int'>
print(type(tipo_lista))      # Saída: <class 'list'>
print(type(tipo_dicionario)) # Saída: <class 'dict'>


cotacaoDolar = 5.50

def converteRealDolar(real):
    return (real / cotacaoDolar).__round__(2)
    
print(converteRealDolar(100))
print(converteRealDolar(200))
print(converteRealDolar(300))
