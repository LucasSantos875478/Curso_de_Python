# analisando se o ano é bissexto

# recebendo o ano
ano = int(input('Digite um ano: '))

# fazendo os testes
if ano % 4 == 0:  # lembrando que a % representa o módulo de uma divisão, ou seja, seu resto
    print(f'O ano {ano} é bissexto')
else:
    print(f'O ano {ano}, não é bissexto')
