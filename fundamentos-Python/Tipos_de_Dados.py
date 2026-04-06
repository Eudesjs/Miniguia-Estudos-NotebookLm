'''
Em Python, existem quatro tipos de dados primitivos comuns, que são os seguintes:
1. **Inteiro (Integer)**: Representa números inteiros, podendo ser positivos ou negativos sem parte
decimal.
2. **Ponto Flutuante (Float)**: Utilizado para números decimais, incluindo números fracionários e
exponentes, como 2.5, -0.3, ou 1.5e-10.
3.**Booleano (Boolean)**: Representa valores lógicos de verdadeiro (True) ou falso (False).
4.**String**: Utilizada para armazenar sequências de caracteres, como palavras, frases e números escritos
como texto.
Adicionalmente, além dos tipos de dados primitivos comuns, Python também oferece suporte a números
complexos, ampliando as possibilidades de cálculos matemáticos mais avançados é essencial compreender
esses tipos de dados, pois são a base para a manipulação e processamento de informações em Python, abrindo caminho para uma ampla variedade
de aplicações que requerem diferentes tipos de dados e operações específicas
Tipos de Dados:
Cada variável em Python possui um tipo de dado, que define o tipo de valor que ela pode armazenar.
Os tipos de dados mais comuns em Python são:
Inteiro (int): Números inteiros, como 1, 2, 3, etc.
Ponto flutuante (float): Números com casas decimais, como 1.5, 2.75, 3.14, etc.
String (str): Textos, como "Olá, mundo!", "Python é legal", etc.
Booleano (bool): Valores True ou False.
Conversão de Tipos:
É possível converter um tipo de dado para outro usando funções específicas.
Exemplo:
'''

nome = 'Eudes' # str
print(nome)
print(type(nome))

numero_inteiro = 10 # int
print(numero_inteiro)
print(type(numero_inteiro))

numero_float = float(numero_inteiro)  # Converte um inteiro para um float
print(numero_float)
print(type(numero_float))