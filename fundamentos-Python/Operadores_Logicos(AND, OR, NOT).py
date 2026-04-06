'''
Os operadores lógicos "AND", "OR" e "NOT" são utilizados em programação para combinar condições e realizar
operações lógicas.
1 - O operador "AND" é usado para combinar duas ou mais condições, e retorna True apenas se todas as
condições forem verdadeiras. Caso contrário, retorna False.
2 - O operador "OR" é usado para combinar duas ou mais condições, e retorna True se pelo menos uma das
condições for verdadeira. Retorna False apenas se todas as condições forem falsas.
3 - O operador "NOT" é usado para inverter o valor de uma condição, ou seja, se a condição for verdadeira,
o "NOT" a torna falsa e vice-versa.
Esses operadores são fundamentais para a criação de expressões lógicas mais complexas e para controlar
o fluxo de um programa com base em múltiplas condições. Eles são amplamente utilizados em estruturas de
controle de fluxo, como condicionais e loops, para tomar decisões e executar determinadas ações com base
nas condições especificadas.
'''
'''
Os operadores lógicos em Python permitem combinar expressões booleanas (True ou False) para formar novas
expressões booleanas. São ferramentas essenciais para tomar decisões e realizar comparações complexas em
seus programas. São eles:
E (and): Retorna True se ambas as expressões forem True.
Exemplo: x > 0 and y < 10.
Ou (or): Retorna True se pelo menos uma das expressões for True.
Exemplo: x == 0 or y == 10.
Não (not): Inverte o valor da expressão.
Exemplo: not (x > 0).
'''

# Operador AND
# O operador "AND" retorna True apenas se ambas as expressões forem verdadeiras. Caso contrário, retorna False.
x = 5
y = 8
print(x > 0 and y < 10)  # Saída: True
print(x > 0 and y > 10)  # Saída: False

# Operador OR
# O operador "OR" retorna True se pelo menos uma das expressões for verdadeira. Retorna False apenas se todas as expressões forem falsas.
x = 5
y = 8
print(x > 0 or y < 10)  # Saída: True
print(x > 0 or y > 10)  # Saída: True

# Operador NOT
# O operador "NOT" inverte o valor da expressão. Se a expressão for verdadeira, o "NOT" a torna falsa e vice-versa.
x = 5
print(not (x > 0))  # Saída: False
print(not (x < 0))  # Saída: True



