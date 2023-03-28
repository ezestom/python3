#Uso de números en Python

demo_int = int('215')
print(demo_int)


demo_float = float('215.3')
print(demo_float)

# Output:
# 215
# 215.3

#!abs() devuelve el valor absoluto de un número
print(abs(39 - 16))
print(abs(16 - 39))

# Output
# 23
# 23

#!round() redondea un número
print(round(14.5))

# Output: 15

#!Biblioteca de Python math
from math import ceil, floor   # Importa solo ceil y floor

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)

# Output
# 13