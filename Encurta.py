#encurtador de links

import pyshorteners

link = input("Digite o link: ")

encurtador = pyshorteners.Shortener()

x = encurtador.tinyurl.short(link)

print("Link encurtado: ", x)
