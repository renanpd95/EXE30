import math

a = int(input("Insira o lado A: "))
b = int(input("Insira o lado B: "))
c = int(input("Insira o lado C: "))

A = math.pow(a,2)
B= math.pow(b,2)
C = math.pow(c,2)

diago = A+B+C

print("Diagonal: ",diago)