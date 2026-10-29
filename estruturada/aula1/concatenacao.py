nome = input('Digite seu nome: ')
sobrenome = input('Digite seu sobrenome: ')
print('Olá,', nome+' '+sobrenome, 'seja bem-vindo(a)!')

#print(nome+5) // ocorre erro, pois não é possível concatenar string com inteiro

print(nome+str(5))  # converte o inteiro para string antes de concatenar
print( '6' + '5' )
print( 6 + 5 )

print(f'Seu sobrenome é {sobrenome}')  # forma mais moderna de concatenar strings
print(f'Seu nome é {nome} e seu sobrenome é {sobrenome}')  # forma ainda mais moderna de concatenar strings

msg = f'Seu nome é {nome} e seu sobrenome é {sobrenome}'  # forma ainda mais moderna de concatenar strings
print(msg)  # forma ainda mais moderna de concatenar strings

n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')

print('Aqui ocorreu uma concatenação. Por que se são números?',n1+n2) # aqui haverá a concatenação dos números, pois eles são strings
print(f'A soma de {n1} + {n2} é igual a {int(n1) + int(n2)}')  # forma ainda mais moderna de concatenar strings