"""Maria está criando um jogo para seus alunos praticarem lógica e pensamento rápido. Ela quer um programa onde o computador escolhe um número aleatório entre 1 e 100, e o jogador tem que adivinhar qual é.

Além de garantir a jogabilidade, Maria deseja que o programa trate erros de entrada, impedindo que o usuário forneça valores inválidos, como letras ou números fora do intervalo permitido.

Sua tarefa é criar um programa que gere um número aleatório entre 1 e 100 e permita que o usuário tente adivinhar o número. O programa deve informar se o palpite é maior ou menor que o número correto, até que o usuário acerte. Se o usuário digitar um valor inválido ou um número fora do intervalo, uma exceção ValueError deve ser lançada ."""

import random
def adivinhar_numero():
    numero_secreto = random.randint(1, 100)
    tentativas = 0  
    print("Bem-vindo ao jogo de adivinhação! Tente adivinhar o número entre 1 e 100.")
    while True:
        try:
            palpite = int(input("Digite seu palpite: "))
            if palpite < 1 or palpite > 100:
                raise ValueError("O número deve estar entre 1 e 100.")
            tentativas += 1
            if palpite < numero_secreto:
                print("Muito baixo! Tente novamente.")
            elif palpite > numero_secreto:
                print("Muito alto! Tente novamente.")
            else:
                print(f"Parabéns! Você acertou o número {numero_secreto} em {tentativas} tentativas.")
                break
        except ValueError as ve:
            print(f"Entrada inválida: {ve}. Por favor, tente novamente.")
adivinhar_numero()