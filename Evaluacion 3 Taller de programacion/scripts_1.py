import time

# ---------------------------------
# SELLO
# ---------------------------------

print("======================================")
print("     ELIAS ORTIZ - B1 - IPLACEX - 2026")
print("======================================")

time.sleep(2)

# ---------------------------------
# Crear lista vacía
# ---------------------------------

lista = []

# ---------------------------------
# Solicitar cantidad de números
# ---------------------------------

while True:

    try:
        N = int(input("\nIngrese la cantidad de números: "))

        if N >= 3:
            break
        else:
            print("Debe ingresar mínimo 3 números.")

    except ValueError:
        print("Error: debe ingresar un número entero.")

# ---------------------------------
# Llenar lista
# ---------------------------------

for i in range(N):

    while True:

        try:
            numero = int(input(f"Ingrese el número {i+1}: "))
            lista.append(numero)
            break

        except ValueError:
            print("Error: ingrese un número válido.")

# ---------------------------------
# 1) Tercer mayor número
# ---------------------------------

lista_ordenada = sorted(lista, reverse=True)

# ---------------------------------
# 2) Números impares
# ---------------------------------

impares = []

for numero in lista:

    if numero % 2 != 0:
        impares.append(numero)

# ---------------------------------
# 3) Números entre dos mayores
# ---------------------------------

numeros_condicion = []

for i in range(1, len(lista) - 1):

    if lista[i - 1] > lista[i] and lista[i + 1] > lista[i]:

        numeros_condicion.append(lista[i])

# ---------------------------------
# Mostrar resultados lentamente
# ---------------------------------

print("\n========== RESULTADOS ==========")

time.sleep(1)

print("\n1) El tercer mayor número ingresado es:")
time.sleep(1)

print(f"   → {lista_ordenada[2]}")
time.sleep(2)

print("\n2) Cantidad de números impares encontrados:")
time.sleep(1)

print(f"   → Total: {len(impares)}")
time.sleep(1)

print(f"   → Números impares encontrados: {impares}")
time.sleep(2)

print("\n3) Números que están entre dos números mayores:")
time.sleep(1)

print(f"   → Números encontrados: {numeros_condicion}")
time.sleep(1)

print(f"   → Cantidad total: {len(numeros_condicion)}")
time.sleep(1)

print("\n===================================")
print("   ELIAS ORTIZ - B1 - IPLACEX - 2026")
print("=====================================")