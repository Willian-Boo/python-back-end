pessoas = {
    "Ana": {"nome": "Ana", "idade": 25, "cidade": "São Paulo"},
    "Bruno":{"nome": "Bruno", "idade": 30, "cidade": "Rio de Janeiro"},
    "Carla":{"nome": "Carla", "idade": 28, "cidade": "Belo Horizonte"},
}

print("Pessoas cadastradas:")
for pessoa in pessoas.values():
    print(f"- Nome: {pessoa['nome']}, Idade: {pessoa['idade']}, Cidade: {pessoa['cidade']}")
print("\nTotal de pessoas cadastradas:", len(pessoas))

#outra forma de iterar
print("\nDetalhes das pessoas cadastradas:")
for nome, detalhes in pessoas.items():
    print(f"Nome: {nome}")
    for chave, valor in detalhes.items():
        print(f"  {chave.capitalize()}: {valor}")
    print()

#exemplo de acesso a chaves
print(pessoa.keys())