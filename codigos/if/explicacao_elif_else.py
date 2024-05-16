# recebendo a idade do usuário e tranformando no tipo inteiro
idade = int(input('Digite a sua idade: '))

# começando o if
if idade < 16:
    print('Você não pode votar')
if idade < 18:
    print('O seu voto é opcional')
else:
    print('Seu voto é obrigatório')
