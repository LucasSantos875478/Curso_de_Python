# Calculando a méida de um aluno e vendo se ele passou

# Pedindo as notas para o usuário
n_1 = float(input('Digite a sua nota: '))
n_2 = float(input('Digite a sua nota: '))
n_3 = float(input('Digite a sua nota: '))
n_4 = float(input('Digite a sua nota: '))
n_5 = float(input('Digite a sua nota: '))

# Calculando a média
media = (n_1 + n_2 + n_3 + n_4 + n_5) / 5

# Testando as notas
if media >= 7:
    print(f'Você passou, a sua média foi {media}')
elif media >= 5:
    print(f'Você está de recuperação, a sua média foi {media}')
else:
    print(f'Você está reprovado, sua média foi {media}')
