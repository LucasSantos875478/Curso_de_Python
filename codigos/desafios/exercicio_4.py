# Exercício 4:
# Pergunte ao usuário um número e mostre a sua divisão normal por 2, sua divisão inteira por 2 e seu módulo por 2

num = int(input('Digite um número: '))

# divisão
div = num / 2

# divisão inteira
div_int = num // 2

# módulo
mod = num % 2

print(f'O número digitado foi {num}, sua divisão é {div}, sua divisão inteira é {div_int} e seu módulo é {mod}')
