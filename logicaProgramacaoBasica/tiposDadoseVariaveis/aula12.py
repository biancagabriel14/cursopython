#exercicio imc + ellipsis 

#luiz otavio tem 1.80 de altura, pesa 95kg, imc é 29,320987654320987

#nome = 'luiz otavio'
#altura = 1.80
#peso = 95

nome = 'bianca'
altura = 1.65
peso = 110

imc = peso/(altura **2)

print(nome, 'tem', altura, 'de altura')
print('pesa', peso, 'quilos e seu imc é: ')
print(imc)

linha1 = f'{nome} tem {altura} de altura'
print(f'{nome} tem {altura:.2f} de altura, pesa {peso} quilos e seu imc é: {imc:.1f}')