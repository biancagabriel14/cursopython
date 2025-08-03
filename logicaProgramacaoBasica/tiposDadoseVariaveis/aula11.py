#precedencia entre operadores aritimeticos

# 1. (n+n) - parenteses
# 2. ** - potencia
# 3. * / // % - multiplicação e divisão
# 4. + - soma e subtração

conta_1 = 1 + 1 ** 5 + 5 #7
conta_2 = (1 + 1) ** (5 + 5) #1024
print(conta_1)
print(conta_2)