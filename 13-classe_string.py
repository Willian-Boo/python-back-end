curso = "PytHon"

print(curso.lower())
print(curso.upper())
print(curso.title())

#REMOVER ESPEÇOS NA STRING
texto = "   Olá mundo!   "
print(texto)
print(texto.strip())
print(texto.rstrip())
print(texto.lstrip())

#CENTER
menu = "Home"
print(menu.center(20, "#"))

#JOIN
curso = "python".capitalize()
print(".".join(curso))