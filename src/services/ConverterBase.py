# Importando a biblioteca necessária para a conversão de base
import base64

# Criando a função para converter binário em decimal
def bin_to_dec(n):
    return int(n, 2)

# Criando a função para converter binário em hexadecimal
def bin_to_hex(n):
    decimal = int(n, 2)
    Decimal = hex(decimal).replace("0x", "")
    return Decimal.upper() 

# Criando a função para converter binário em octal
def bin_to_octal(n):
    decimal = int(n, 2)
    return oct(decimal).replace("0o", "")

# Criando a função para converter binário em quaternário
def bin_to_quaternary(n):
    decimal = int(n, 2)
    quaternary = ""
    while decimal > 0:
        quaternary = str(decimal % 4) + quaternary
        decimal //= 4
    return quaternary

# Criando a função para converter binário em base 32
def bin_to_base32(n):
    decimal = int(n, 2)
    b32 = base64.b32encode(decimal.to_bytes((decimal.bit_length() + 7) // 8, 'big')).decode('utf-8')
    return b32.upper()

# Criando a função para converter binário em base 64
def bin_to_base64(n):
    decimal = int(n, 2)
    b64 = base64.b64encode(decimal.to_bytes((decimal.bit_length() + 7) // 8, 'big')).decode('utf-8')
    return b64.upper()

# Testando as funções
'''
n = "0101011111011111000011001"

print(f"Binário: {n}")
print(f"Quaternário: {bin_to_quaternary(n)}")
print(f"Octal: {bin_to_octal(n)}")
print(f"Decimal: {bin_to_dec(n)}")
print(f"Hexadecimal: {bin_to_hex(n)}")
print(f"Base 32: {bin_to_base32(n)}")
print(f"Base 64: {bin_to_base64(n)}")
'''