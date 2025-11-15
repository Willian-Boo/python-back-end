# FOR
texto = input("Informe um texto: ")
VOGAIS = "AEIOU"

for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra.upper(), end="-")
print(" ")
print(f"-"*40)

#RANGE
print("RANGE")
print(list(range(0, 51, 5)))

#while
print(f"-"*40)
opcao = -1
while opcao !=0:
    opcao = int(input("[1] Sacar \n[2] Extrato \n[0] Sair \n: "))
    if opcao == 1:
        print("Sacando ...")
    elif opcao == 2:
        print("Exibindo extrato ...")
    elif opcao == 0:
        print("Obrigado por usar nosso sistema")
        break
    else:
        print("Opção inválida")
else:
    print("Até logo")