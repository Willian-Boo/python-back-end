nome = "Willian"
idade = 35
profissao = "Programador"
linguagem = "Python"

PI = 3.14159

print("Olá meu nome é %s tenho %d anos, sou %s e utilizo a linguagem %s nos meus projetos" % (nome, idade, profissao, linguagem))

print("Olá meu nome é {} tenho {} anos, sou {} e utilizo a linguagem {} nos meus projetos".format(nome, idade, profissao, linguagem))

print("Olá meu nome é {3} tenho {0} anos, sou {2} e utilizo a linguagem {1} nos meus projetos".format(idade, linguagem, profissao, nome))

print(f"Olá meu nome é {nome} tenho {idade} anos, sou {profissao} e utilizo a linguagem {linguagem} nos meus projetos")

print(PI)
print(f"O valor de PI: {PI:.2f}")

