import time

# ---------------------------------
# SELLO
# ---------------------------------

print("======================================")
print("     ELIAS ORTIZ - B1 - IPLACEX 2026")
print("======================================")

time.sleep(2)

# ---------------------------------
# FUNCIÓN PARA INGRESAR NOTAS
# ---------------------------------

def ingresar_notas(N):

    notas = []

    for i in range(N):

        nota = float(input(f"Ingrese la nota {i+1}: "))
        notas.append(nota)

    return notas

# ---------------------------------
# FUNCIÓN PARA CALCULAR PROMEDIO
# ---------------------------------

def calcular_promedio(lista):

    suma = 0

    for numero in lista:
        suma += numero

    promedio = suma / len(lista)

    return promedio

# ---------------------------------
# FUNCIÓN PARA OBTENER NOTAS
# BAJO EL PROMEDIO
# ---------------------------------

def notas_bajo_promedio(lista):

    promedio = calcular_promedio(lista)

    menores = []

    for numero in lista:

        if numero < promedio:
            menores.append(numero)

    return menores

# ---------------------------------
# PROGRAMA PRINCIPAL
# ---------------------------------

N = int(input("\nIngrese la cantidad de notas: "))

notas = ingresar_notas(N)

promedio = calcular_promedio(notas)

notas_menores = notas_bajo_promedio(notas)

# ---------------------------------
# MOSTRAR RESULTADOS
# ---------------------------------

print("\n========== RESULTADOS ==========")

time.sleep(1)

print("\nNotas ingresadas:")
time.sleep(1)

print(f"→ {notas}")

time.sleep(2)

print("\nPromedio de las notas:")
time.sleep(1)

print(f"→ {round(promedio,2)}")

time.sleep(2)

print("\nNotas que están bajo el promedio:")
time.sleep(1)

print(f"→ Promedio general: {round(promedio,2)}")

time.sleep(1)

print(f"→ Notas bajo el promedio: {notas_menores}")

time.sleep(1)

print(f"→ Cantidad de notas bajo el promedio: {len(notas_menores)}")

time.sleep(1)

print("\n================================")
print("   ELIAS ORTIZ - B1 - IPLACEX 2026")
print("================================")