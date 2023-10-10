import math

numero = int(input("Digita el numero: "))

while numero < 0 or numero > 10:
    print("Error --> debe ser positivo")
    numero = int(input("Digita el numero: "))
# .2f entrega dos decimales
print(f"\n Su raiz cuadrada es: {(math.sqrt(numero)):.2f}")



#ejemplo 2
i = 0
while i<10:
    print(i)
    i += 15




#while True:
#    frase = input("Introduce algo: ")
#    if frase == "salir":
#        break
#    print(frase)