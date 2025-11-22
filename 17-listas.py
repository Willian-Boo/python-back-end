frutas = ["laranja", "maça", "uva"]

letras = list("python")

#acesso direto na lista
frutas[0]
print(frutas[0]) # "laranja"
print(frutas[-1]) # "uva"

#fatiamento
print(letras[:2])

#append adiciona itens na lista
frutas.append("banana")
print(frutas)

#copy faz uma cópia da lista
frutas_copy = frutas.copy()
print(frutas_copy)

#clear limpa a lista
frutas_copy.clear()
print(frutas_copy)

#count conta quantas vezes um item aparece na lista
print(frutas.count("maça"))  # Conta quantas vezes "maça" aparece na lista

#extend junta a lista
frutas.extend(["kiwi", "abacaxi"])
print(frutas)

#index
frutas.index("uva")  # Retorna o índice do primeiro elemento "uva"
print(frutas.index("uva"))

#pop
frutas.pop()  # Remove o último elemento da lista
print(frutas)

#remove, retira o elemento passando o valor do item
frutas.remove("maça")  # Remove o primeiro elemento "maça"
print(frutas)

#reverse, inverte a ordem
frutas.reverse()
print(frutas)

#sort, ordenar a lista
frutas.sort()  # Ordena a lista em ordem alfabética
print(frutas)