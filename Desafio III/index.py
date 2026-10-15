from math import prod

def fatores_comuns(a, b):
    fator = 2
    while fator <= a and fator <= b:
        if a % fator == 0 and b % fator == 0:
            yield fator
            a //= fator
            b //= fator
        else:
            fator += 1
          
a, b = 40, 60
lista = list(fatores_comuns(a, b))

print("Fatores comuns:", lista)
print("MDC:", prod(lista))
