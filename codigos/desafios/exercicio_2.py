# Exercício 2:
# Peça ao usuário 3 notas e mostre a sua média e também as suas 3 notas

# perguntando as notas ao usuário e armazenando em variáveis
nota_1 = float(input('Qual a sua nota? '))
nota_2 = float(input('Qual a sua nota? '))
nota_3 = float(input('Qual a sua nota? '))

# calculando a média do usuário
media = (nota_1 + nota_2 + nota_3) / 3

# mostrando a resposta para o usuário
print(f'Suas notas foram: {nota_1}, {nota_2}, {nota_3}. Sua média foi {media}')
