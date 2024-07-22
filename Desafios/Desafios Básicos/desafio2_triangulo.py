''' 

Desafio
Leia 3 valores reais (A, B e C) e verifique se eles formam ou não um triângulo. Em caso positivo, calcule o perímetro do triângulo (soma de todos os lados) e apresente a mensagem:

Perimetro = XX.X

Em caso negativo, calcule a área do trapézio que tem A e B como base e C como altura, mostrando a mensagem:

Area = XX.X

Fórmula da área de um trapézio: AREA = ((A + B) x C) / 2

'''

# Abaixo segue um exemplo de código que você pode ou não utilizar
lados = [float(x) for x in input().split()]

a = lados[0];
b = lados[1];
c = lados[2];

# TODO: Para o cálculo do perímetro triangular aplique seus conhecimentos em Estruturas Condicionais, 
# e complete os espaços em branco com as operações que solucionam o desafio.
if a + b > c and  a + c > b  and b + c > a:
    # Calcule o perímetro do triângulo
    perimetro = a + b + c
    print(f"Perimetro = {perimetro:.1f}")
else:
    # Calcule a área do trapézio
    area = ((a + b) * c) / 2
    print(f"Area = {area:.1f}")