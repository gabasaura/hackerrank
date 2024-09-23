def flippingBits(n):
    return n ^ 4294967295

print('====== TEST ======')
print(flippingBits(2147483647))  # Output: 2147483648
print(flippingBits(1))           # Output: 4294967294
print(flippingBits(0))           # Output: 4294967295

# XOR (^) es un operador bit a bit que compara los bits de dos números.
# XOR devuelve 1 si los bits son diferentes y 0 si son iguales.

# 4294967295 es el número máximo de 32 bits sin signo, en binario: 11111111111111111111111111111111
# Aplicar XOR entre un número n y 4294967295 invierte todos los bits de n.
# Esto es útil para "voltear" los bits de un número de 32 bits.

# Ejemplo:
# n = 5 en binario: 00000000000000000000000000000101
# 4294967295 en binario: 11111111111111111111111111111111
# Resultado de n ^ 4294967295: 11111111111111111111111111111010 (que es 4294967290 en decimal)

# Esta operación invierte los bits de n.