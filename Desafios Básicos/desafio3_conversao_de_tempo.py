''' 

Desafio
Você terá o desafio de ler um valor inteiro, que é o tempo de duração em segundos de um determinado evento em uma loja, e informe-o expresso no formato horas:minutos:segundos.

'''

# Abaixo segue um exemplo de código que você pode ou não utilizar
segundos = int(input())

# TODO: Complete os espaços em branco com as operações que calculam a duração em segundos.
# Calcula os minutos
minutos = segundos // 60
segundos = segundos - (minutos * 60)  # Calcula os segundos restantes

# Calcula as horas
horas = minutos // 60
minutos = minutos - (horas * 60)  # Calcula os minutos restantes

# Imprime o resultado no formato horas:minutos:segundos
print("{}:{}:{}".format(horas, minutos, segundos))