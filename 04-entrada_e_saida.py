#criando um input
nome = input("Informe o seu nome: ")
sobrenome = input("Informe seu sobrenome: ")
idade = input("Informe a sua idade: ")

print(f"Olá {nome} {sobrenome}")
print(nome,idade, end="...\n")
print(nome,sobrenome, sep="-")