# Função simples em Python
def exibir_mensagem():
    print("Olá! Esta é uma função simples em Python.")
exibir_mensagem()

# Função com parâmetros
def saudacao(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a).")
saudacao("Maria")

# Função com retorno de valor
def soma(a, b):
    return a + b
resultado = soma(5, 3)
print(f"A soma de 5 e 3 é: {resultado}")

# Função com valor padrão para parâmetro
def potencia(base, expoente=2):
    return base ** expoente
print(f"2 elevado ao quadrado é: {potencia(2)}")
print(f"3 elevado ao cubo é: {potencia(3, 3)}")

# Função com múltiplos retornos
def operacoes(a, b):
    soma = a + b
    produto = a * b
    return soma, produto
s, p = operacoes(4, 5)
print(f"Soma: {s}, Produto: {p}")

# Função com argumentos variáveis
def carro(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")
carro(marca="Toyota", modelo="Corolla", ano=2020)
carro(marca="Honda", modelo="Civic", cor="Preto", ano=2019)

# Função com argumentos nomeados
def informacoes_pessoa(nome, idade, cidade):
    print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")