def contagem(texto):
    return texto.lower().count('a')

texto = input("Digite a frase: ")
quantidade = contagem(texto)

print(f"Na string {texto} a letra 'A' aparece {quantidade} vezes")