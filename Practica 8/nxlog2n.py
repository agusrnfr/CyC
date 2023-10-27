import numpy as np
from scipy.optimize import fsolve
import math
import argparse

def equation_to_solve(n, h):
    return n * np.log2(n) - h * 1000000

# Configurar el análisis de argumentos
parser = argparse.ArgumentParser()
parser.add_argument("-H", "--h_value", type=float, default=1, help="Valor de h (por defecto: 1)")
args = parser.parse_args()

h = args.h_value  # Obtener el valor de h desde los argumentos

# Establecer una estimación inicial para fsolve
initial_guess = 1000

# Usar fsolve para encontrar la solución de n * log2(n) = 1000000
result = fsolve(equation_to_solve, initial_guess, args=(h,))

print("La solución aproximada es:", result)
print("La solución en notación científica es:", "{:.4e}".format(result[0]))

desired_value = h * 1000000
n = 1
factorial_value = 1

while factorial_value <= desired_value:
    n += 1
    factorial_value *= n

n -= 1  # Restar 1 para redondear

print("La solución exacta es:", n)