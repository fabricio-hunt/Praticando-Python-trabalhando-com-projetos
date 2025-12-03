"""Pedro está desenvolvendo um sistema de cadastro e precisa gerar senhas seguras para os usuários. Ele quer um programa que crie senhas aleatórias com letras maiúsculas, minúsculas, números e caracteres especiais.

Crie um programa que gere uma senha aleatória de 12 caracteres, contendo pelo menos uma letra maiúscula, uma minúscula, um número e um caractere especial. Exiba a senha gerada."""

import random
import string   
def gerar_senha(tamanho=12):
    if tamanho < 4:
        raise ValueError("O tamanho da senha deve ser pelo menos 4 para incluir todos os tipos de caracteres.")

    letras_maiusculas = string.ascii_uppercase
    letras_minusculas = string.ascii_lowercase
    numeros = string.digits
    caracteres_especiais = string.punctuation

    # Garantir que a senha tenha pelo menos um de cada tipo de caractere
    senha = [
        random.choice(letras_maiusculas),
        random.choice(letras_minusculas),
        random.choice(numeros),
        random.choice(caracteres_especiais)
    ]

    # Preencher o restante da senha com uma mistura aleatória de todos os tipos de caracteres
    todos_os_caracteres = letras_maiusculas + letras_minusculas + numeros + caracteres_especiais
    senha += random.choices(todos_os_caracteres, k=tamanho - 4)

    # Embaralhar a lista para garantir que a ordem dos caracteres seja aleatória
    random.shuffle(senha)

    return ''.join(senha)
senha_gerada = gerar_senha(12)
print("Senha gerada:", senha_gerada)    
