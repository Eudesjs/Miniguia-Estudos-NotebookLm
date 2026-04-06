'''
Operadores de associação são utilizados em linguagens de programação para verificar se um determinado
valor está contido em uma coleção de valores, como uma lista, conjunto ou dicionário. Os operadores de
associação comuns são "in" e "not in". Eles retornam um valor booleano, verdadeiro se o valor estiver
presente na coleção e falso caso contrário. Esses operadores são úteis para verificar a existência de
um elemento em uma estrutura de dados e tomar decisões com base nessa verificação.
'''
'''
Os operadores de associação in e not in em Python permitem verificar se um elemento está presente ou não
em uma coleção, como listas, tuplas, dicionários e strings. São ferramentas úteis para filtrar dados e
realizar comparações em seus programas. Assim como os aoperadores de comparação eles retornam Verdadeiro
(True) ou Falso (False)
'''

# Operador in
'''
O operador "in" é utilizado em programação para verificar se um determinado valor está presente em uma
sequência, como uma lista, tupla, string, dicionário, entre outros. Quando utilizado, o operador "in"
retorna True se o valor estiver presente na sequência e False caso contrário. Por exemplo, podemos usar
o operador "in" para verificar se um elemento está contido em uma lista, se uma chave está presente em
um dicionário, ou se um caractere está em uma string. Este operador é comumente utilizado em estruturas
de controle de fluxo, como condicionais e loops, para verificar a presença de um valor em uma sequência.
'''

frutas = ['maçã', 'banana', 'laranja']
print('maçã' in frutas)  # Saída: True
print('uva' in frutas)   # Saída: False

# Operador not in
print('maçã' not in frutas)  # Saída: False
print('uva' not in frutas)   # Saída: True

# Operador not in
'''
O operador "not in" é utilizado em programação para verificar se um determinado valor não está presente
em uma sequência, como uma lista, tupla, string, dicionário, entre outros. Quando utilizado, o operador
"not in" retorna True se o valor não estiver presente na sequência e False caso contrário. Por exemplo,
podemos usar o operador "not in" para verificar se um elemento não está contido em uma lista, se uma
chave não está presente em um dicionário, ou se um caractere não está em uma string. Este operador é
comumente utilizado em estruturas de controle de fluxo, como condicionais e loops, para verificar a
ausência de um valor em uma sequência.
'''
frutas = ['maçã', 'banana', 'laranja']
print('maçã' not in frutas)  # Saída: False
print('uva' not in frutas)   # Saída: True


