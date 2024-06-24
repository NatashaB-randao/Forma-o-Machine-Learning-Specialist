# # A linguagem R é uma linguagem Interpretada.

# objeto1 <- 3 * 3
# print(objeto1)

# objeto2 <- 2 * 2
# print(objeto2)

# objeto3 <- objeto1 + objeto2
# print(objeto3)

#

# Volume de um tubo
# Seja um tubo com raio de 10 cm, com 1,5 metros de comprimento e com uma espessura de 1 cm. Qual o volume deste cubo? # nolint
# Volume = π * raio² * altura
# π = 3.14 # nolint

raio <- 10
comprimento <- 150
espessura <- 1


volume <- pi * (raio - espessura) ^ 2 * comprimento

print(volume)