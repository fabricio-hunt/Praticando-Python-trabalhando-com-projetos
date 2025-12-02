# Este programa lê um texto digitado pelo usuário e conta o número de vogais (a, e, i, o, u).

texto = input("Digite um texto: ")

def contar_vogais(texto):
    """Conta quantas vogais tem no texto."""
    return sum(1 for letra in texto if letra.lower() in "aeiou")

print(f"O texto contém {contar_vogais(texto)} vogais.")
