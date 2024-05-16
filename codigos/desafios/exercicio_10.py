# desconto para a loja

# recebendo o valor gastado, se a pessoa tem um cadastro e sua idade
cadastro = input('Você é cadastrado na loja: [s/n] ')
idade = int(input('Qual a sua idade: '))
valor_gasto = float(input('Qual o valor gastado na compra: '))

# 1ª forma de resolver

if cadastro == 's':
    if idade >= 18:
        if valor_gasto >= 50:
            print('Você recebeu um desconto')
        else:
            print('Você não recebeu um desconto')
    else:
        print('Você não recebeu um desconto')
else:
    print('Você não recebeu um desconto')

# 2ª forma de resolver
if cadastro == 's' and idade >= 18 and valor_gasto >= 50:
    print('Você recebeu um desconto')
else:
    print('Você não recebeu um desconto')
