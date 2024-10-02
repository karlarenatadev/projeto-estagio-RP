lista1 = [1, 3, 5, 7]

def next_element():
    n = lista1[1] - lista1[0]
    a = lista1[-1] + n
    lista1.append(a)
    return lista1

print(next_element())

lista2 = [2, 4, 8, 16, 32, 64]

def next_element2():
    b = lista2[5] * 2
    lista2.append(b)
    return lista2
print(next_element2())

lista3 = [0, 1, 4, 9, 16, 25, 36]

def soma_quadrados(n):
    quadrados = [i**2 for i in range(n + 1)]
    return quadrados

print(soma_quadrados(7))

lista4 = [4, 16, 36, 64]

def next_element4(n):
    nova = [((i*2)**2) for i in range(n+1)]
    return nova
print(next_element4(5))

lista5 = [1, 1, 2, 3, 5, 8]

def next_element5():
    novo_elemento = lista5[-1] + lista5[-2]
    lista5.append(novo_elemento)
    return lista5
print(next_element5())

lista6 = [2,10, 12, 16, 17, 18, 19]

def next_element6():
    novo_elemento2 = lista6[6] + 1
    lista6.append(novo_elemento2)
    return lista6
print(next_element6())