# Exercício 3:
# Peça ao usuário um núemro e mostre seu sucessor, antecessor, dobro, cubo e sua raíz.

num = int(input('Digite um número: '))

suc = num + 1
ant = num - 1
dob = num * 2
cubo = num ** 3
# usando a propriedade que se elevarmos algo por meio será sua raíz
raiz = num ** (1/2)

print(f'O número digitado foi: {num}, seu sucessor é {suc}, seu antecessor é {ant}, o seu dobro é {dob}, o seu cubo é '
      f'{cubo} e sua raíz é {raiz}')
