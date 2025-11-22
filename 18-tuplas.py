frutas = ("maça", "banana", "laranja", "uva", "pera", "manga", "abacaxi", "kiwi", "morango", "cereja", "pêssego", "ameixa", "melancia", "melão", "framboesa", "amora", "tangerina", "coco")
print("Frutas disponíveis:")
for fruta in frutas:
    print("-", fruta)
print("\nTotal de frutas disponíveis:", len(frutas))
print("\nFrutas em posições específicas:")
print("Primeira fruta:", frutas[0])
print("Quinta fruta:", frutas[4])
print("Última fruta:", frutas[-1])
print("\nFrutas do terceiro ao sétimo:")
for fruta in frutas[2:7]:
    print("-", fruta)
print("\nFrutas em ordem alfabética:")
for fruta in sorted(frutas):
    print("-", fruta)