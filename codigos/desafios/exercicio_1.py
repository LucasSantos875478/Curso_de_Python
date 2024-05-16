# Exercício 1:
# Peça ao usuário o seu nome, idade e mostre as seguintes informações: uma saudação com o nome da pessoa e o ano em
# que a pessoa nasceu.

# pegamos o nome do usuário e deixamos como str
nome = input('Qual o seu nome? ')

# pegamos a idade do usuário e convertemos para o tipo int
idade = int(input('Qual a sua idade no final do ano? '))

# vou deixar o ano em uma variável
ano = 2024

# usei o print para mostrar a resposta, junto com as chaves para poder usar as variáveis
print(f'Olá {nome}, você disse que tem {idade} anos, então você nasceu em {ano - idade}')
