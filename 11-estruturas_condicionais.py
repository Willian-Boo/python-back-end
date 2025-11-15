# IF, apenas uma condição
MAIOR_IDADE = 18
print(f"-"*40)
idade = int(input("Informe sua idade: "))
if idade >= MAIOR_IDADE:
    print("Você é maior de idade")

#IF e ELSE
print(f"-"*40)
if idade >= MAIOR_IDADE:
    print(f"Você tem {idade} anos e é maior de idade")
else:
    print(f"Você tem apenas {idade} anos, ainda é menor de idade")

#IF E ELIF
print(f"-"*40)
if idade > MAIOR_IDADE:
    print(f"Você tem mais de {MAIOR_IDADE} anos de idade")
elif idade == MAIOR_IDADE:
    print(f"Você tem exatamente {MAIOR_IDADE} anos")
elif idade <= 0:
    print("Idade inválida")
else:
    print(f"Você tem menos de {MAIOR_IDADE} anos de idade")

#IF TERNÁRIO
print(f"-"*40)
nota = 7

status = "Aprovado" if nota >= 6 else "reprovado"
print(f"{status} no teste")

print(f"-"*40)
saldo = 2000
opcao = int(input("\n[1] Sacar: \n[2] Extrato: \nInforme uma opção:"))
if opcao == 1:
    saque = float(input("Informe o valor do saque: "))
    if saque <= saldo:
        saldo_atual = saldo-saque
        print(f"Saque de {saque} foi realizado com sucesso")
        print(f"Seu saldo atual é de {saldo_atual}")
    else:
        print("Saldo insuficiente")
elif opcao == 2:
    print(f"Seu saldo é de {saldo}")

