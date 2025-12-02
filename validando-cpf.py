cpf = input("Digite o número de CPF (apenas números): ")

if not cpf.isdigit():
    print("Erro: O CPF deve conter apenas números.")
elif len(cpf) != 11:
    print("Erro: O CPF deve conter exatamente 11 dígitos numéricos.")
else:
    print("CPF informado está no formato correto.")