nome = input('Digte seu nome')
idade = input('Digite sua idade')
peso = input('Digite seu peso')
altura = input('Digite sua altura')

imc = float(peso) / (float(altura) ** 2)
print('Olá,', nome, 'seu IMC é:', imc)

if imc < 18.5:
    print('Você está abaixo do peso')
elif imc < 25:
    print('Você está com o peso normal')
elif imc < 30:
    print('Você está com sobrepeso')
else:
    print('Você está obeso')