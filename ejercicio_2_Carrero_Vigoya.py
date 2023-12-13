# ejercio_2
import random
N = 1000
A = []
for i in range(N):
    val = random.randint(0, 511)
    A.append(val)

# Ejercicio 2: Calcular el valor RMS
import math
rms = math.sqrt(sum(x**2 for x in A) / N) / 511.0  # Normalizar a voltios

print(f"Valor RMS de la señal en voltios: {rms:4f} V")
