a = 'A'
b = 'B'
c = 1.1
formato = 'a={} b={} c={:.2f}'.format(a,b,c)
print(formato)

nome = "Luiz"
idade = 23
formato = '{1} tem {0} anos'
print(formato.format(nome, idade))


nome = "Luiz"
idade = 23
formato = '{n} tem {i} anos'
print(formato.format(n=nome, i=idade))