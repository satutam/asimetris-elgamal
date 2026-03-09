# Implementasi ElGamal murni dengan aritmatika dasar dan Extended GCD

import random

# Fungsi cek bilangan prima
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# Fungsi menghasilkan semua bilangan prima dalam rentang
def primes_in_range(start, end):
    primes = []
    for num in range(start, end+1):
        if is_prime(num):
            primes.append(num)
    return primes

# Modular exponentiation (x^y mod p)
def mod_exp(x, y, p):
    result = 1
    x = x % p
    while y > 0:
        if y % 2 == 1:
            result = (result * x) % p
        y = y // 2
        x = (x * x) % p
    return result

# Extended Euclidean Algorithm untuk invers modular
def extended_gcd(a, m):
    """
    Menghitung invers modular a mod m menggunakan Extended Euclidean Algorithm
    Jika a dan m coprime, invers modulo ada dan dikembalikan
    """
    m0 = m
    x0, x1 = 0, 1
    if m == 1:
        return 0
    while a > 1:
        q = a // m
        t = m
        m = a % m
        a = t
        t = x0
        x0 = x1 - q * x0
        x1 = t
    if x1 < 0:
        x1 += m0
    return x1

# Enkripsi ElGamal
def encrypt(message, p, g, y):
    k = random.randint(1, p-2)  # ephemeral key
    a = mod_exp(g, k, p)
    b = (message * mod_exp(y, k, p)) % p
    return (a, b)

# Dekripsi ElGamal
def decrypt(cipher, x, p):
    a, b = cipher
    s = mod_exp(a, x, p)
    s_inv = extended_gcd(s, p)  # menggunakan fungsi extended_gcd untuk invers modular
    message = (b * s_inv) % p
    return message

# Program Utama
if __name__ == "__main__":
    # Input rentang bilangan prima
    start = int(input("Masukkan batas awal bilangan prima: "))
    end = int(input("Masukkan batas akhir bilangan prima: "))
    prime_list = primes_in_range(start, end)
    print(f"Bilangan prima dalam rentang: {prime_list}")

    # Pilih bilangan prima p
    p = int(input("Pilih bilangan prima p dari daftar di atas: "))

    # Input generator g
    g = int(input(f"Masukkan generator g (1 < g < p, default 2): ") or 2)

    # Kunci privat Alice
    x = random.randint(1, p-2)
    # Kunci publik
    y = mod_exp(g, x, p)

    print(f"\nPublic key: (p={p}, g={g}, y={y})")
    print(f"Private key: x={x}\n")

    # Input pesan numerik
    m = int(input(f"Masukkan pesan numerik (harus < p={p}): "))
    print(f"Original message: {m}")

    # Enkripsi
    cipher = encrypt(m, p, g, y)
    print(f"Ciphertext: {cipher}")

    # Dekripsi
    decrypted = decrypt(cipher, x, p)
    print(f"Decrypted message: {decrypted}")