#if / elif / else 

entrada = input('você quer "entrar" ou "sair"? ')

if entrada == 'entrar':
    print('você entrou no sistema')
    print(12341234)
elif entrada == 'sair':
    print('você saiu do sistema')
else:
    print('você não digitou nem entrar ou sair')    

print('FORA DO BLOCO')