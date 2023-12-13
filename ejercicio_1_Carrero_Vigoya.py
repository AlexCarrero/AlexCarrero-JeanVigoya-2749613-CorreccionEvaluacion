# ejercicio_1
import random
N = 1000
A = []
for i in range(N):
    val = random.randint(0, 511)
    A.append(val)

# Ejercicio 1
# Tensión máxima
tension_maxima = max(A) / 511.0  # Normalizar a voltios
print(f"Tensión máxima medida en voltios: {tension_maxima:4f} V")

# Tensión mínima
tension_minima = min(A) / 511.0  # Normalizar a voltios
print(f"Tensión mínima medida en voltios: {tension_minima:4f} V")

# Tensión promedio
tension_promedio = sum(A) / len(A) / 511.0  # Normalizar a voltios
print(f"Tensión promedio medida en voltios: {tension_promedio:4f} V")