# Verificando se é obrigatório votar

# Recebendo a idade da pessoa
idade = int(input('Qual a sua idade: '))

# Fazendo os testes de acordo com as regras eleitorais no Brasil
if idade < 16:
    print('Você não pode votar.')  # Menores de 16 anos não podem votar
elif idade < 18 or idade > 70:
    print('Seu voto é opcional.')  # Voto é opcional para menores de 18 ou maiores de 70
else:
    print('Seu voto é obrigatório.')  # Voto obrigatório para quem tem entre 18 e 70 anos
