# verificando se é obrigatório votar

# recebendo a idade da pessoa
idade = int(input('Qual a sua idade: '))

# fazendo os testes
if idade < 16:
    print('Você não pode votar')
elif idade < 18 or idade > 70:
    print('Seu voto é opcional')
else:
    print('seu voto é obrigatório')
