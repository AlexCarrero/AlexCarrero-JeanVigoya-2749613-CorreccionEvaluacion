# ejercicio_3
valor_pico_pico = float(input("Ingrese el valor pico a pico de la onda sinusoidal: "))

# Generar datos de una onda sinusoidal
frecuencia = 1.0  # Frecuencia de la onda
tiempo = 1.0      # Duración de la onda en segundos
N = 1000          # Número de puntos en la onda
import math
A = [valor_pico_pico * math.sin(2 * math.pi * frecuencia * t / N) for t in range(N)]

# Calcular el valor RMS utilizando el código del ejercicio 2
import math
rms_calculado = math.sqrt(sum(x**2 for x in A) / N) / valor_pico_pico

# Calcular el valor RMS teórico utilizando la ecuación (2)
rms_teorico = valor_pico_pico / (2 * math.sqrt(2))

# Calcular el porcentaje de error
porcentaje_error = ((rms_teorico - rms_calculado) / rms_teorico) * 100

# Mostrar resultados
print(f"Valor RMS calculado: {rms_calculado:.4f} V")
print(f"Valor RMS teórico (ecuación 2): {rms_teorico:4f} V")
print(f"Porcentaje de error: {abs(porcentaje_error):4f}%")
