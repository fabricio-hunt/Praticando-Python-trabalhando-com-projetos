"""Calculando a gorjeta em um restaurante"""
print("Calculando a gorjeta em um restaurante")
total_conta = float(input("Qual o valor da conta? "))
porcentagem_gorjeta = float(input("Qual a porcentagem de gorjeta? "))
gorjeta = total_conta * (porcentagem_gorjeta / 100)
print(f"A gorjeta é de R$ {gorjeta:.2f}")
print(f"O total da conta é de R$ {total_conta + gorjeta:.2f}")      
    