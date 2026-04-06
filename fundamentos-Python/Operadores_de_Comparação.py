'''
Operadores de comparação são símbolos utilizados em programação para comparar dois valores e determinar
se eles são iguais, diferentes, maiores, menores ou maiores ou iguais. Alguns exemplos de operadores de
comparação são:
== (igual), != (diferente), > (maior), < (menor), >= (maior ou igual) e <= (menor ou igual).
Esses operadores são muito úteis para a criação de condições e tomada de decisões em um programa.
'''
'''
Os operadores de comparação em Python permitem verificar se duas expressões são iguais, diferentes,
maiores, menores, etc. São ferramentas essenciais para tomar decisões e realizar comparações em seus
programas. Retornam com resultado verdadeiro (True) ou Falso (False) (tipo bool)
'''

# Exemplo de operadores de comparação em Python

# Igualdade ( == )
x = 10
y = 20
igualdade = x == y
print("Igualdade:", igualdade)  # Saída: Igualdade: False

# Diferença ( != )
diferenca = x != y
print("Diferença:", diferenca)  # Saída: Diferença: True

# Maior ( > )
maior = x > y
print("Maior:", maior)  # Saída: Maior: False

# Menor ( < )
menor = x < y
print("Menor:", menor)  # Saída: Menor: True

# Maior ou Igual ( >= )
maior_ou_igual = x >= y
print("Maior ou Igual:", maior_ou_igual)  # Saída: Maior ou Igual: False

# Menor ou Igual ( <= )
menor_ou_igual = x <= y
print("Menor ou Igual:", menor_ou_igual)  # Saída: Menor ou Igual: True

# Operador de Identidade ( is )

'''
O operador de identidade "is" é utilizado em programação para verificar se dois objetos têm a mesma
identidade, ou seja, se estão armazenados no mesmo local na memória. Em Python, por exemplo, o
operador "is" compara os endereços de memória dos objetos em questão, enquanto o operador de igualdade
"==" compara os valores dos objetos. O uso do operador "is" é útil em situações em que se deseja
verificar se duas variáveis estão se referindo ao mesmo objeto, e não apenas se possuem o mesmo valor.
'''
a = 7 # int
b = 7.0 # float
print(a is b) # (IS) A é B?
print(a == b) # (==) A é igual a B?

# Operador de Identidade ( is not)
# Operador de identidade (is not)
'''
O operador de identidade "is not" é utilizado em programação para verificar se dois objetos não têm a
mesma identidade, ou seja, se não estão armazenados no mesmo local na memória. Em Python, por exemplo,
o operador "is not" é o oposto do operador "is" e também compara os endereços de memória dos objetos em
questão. Ele retorna True se os objetos não são os mesmos e False se forem os mesmos. O uso do operador
"is not" é útil em situações em que se deseja verificar se duas variáveis não estão se referindo ao mesmo
objeto.
'''
a = 7 # int
b = 7.0 # float
print(a is not b) # (is not) A não é B?
print(a != b) # (!=) A é diferente de B?