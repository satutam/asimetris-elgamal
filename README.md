# ElGamal Kriptografi - Implementasi Algoritma Murni

## Usage
Repositori ini berisi implementasi **ElGamal** untuk enkripsi dan dekripsi menggunakan aritmatika murni, tanpa library eksternal.  
Fungsi utama yang tersedia:  

- `encrypt(message, p, g, y)` → Enkripsi pesan  
- `decrypt(cipher, x, p)` → Dekripsi pesan  
- `extended_gcd(a, m)` → Menghitung invers modular  
- `mod_exp(x, y, p)` → Modular exponentiation  

Contoh penggunaan:

```python
from elgamal import encrypt, decrypt, extended_gcd, mod_exp

p = 467
g = 2
x = 127                  # kunci privat
y = mod_exp(g, x, p)     # kunci publik

message = 123
cipher = encrypt(message, p, g, y)
decrypted = decrypt(cipher, x, p)

print("Cipher:", cipher)
print("Pesan terdekripsi:", decrypted)
````

---

## ElGamal Theory

ElGamal didasarkan pada teori bilangan:

* Pilih bilangan prima `p` dan generator `g`.
* Pilih kunci privat `x` sehingga `1 <= x <= p-2`.
* Hitung kunci publik:

```text
y = g^x mod p
```

* Enkripsi pesan `m` menjadi cipher `(a, b)`:

```text
a ≡ g^k mod p
b ≡ m * y^k mod p
```

* Dekripsi cipher `(a, b)`:

```text
m ≡ b * (a^x)^-1 mod p
```

Kunci publik: `(p, g, y)`
Kunci privat: `x`

---

## Contoh Pembuatan Kunci

### Langkah 1: Pilih bilangan prima dan generator

```python
p = 467
g = 2
```

### Langkah 2: Pilih kunci privat Alice

```python
x = 127  # contoh acak 1 <= x <= p-2
```

### Langkah 3: Hitung kunci publik

```python
y = g^x mod p = 2^127 mod 467 = 58
```

Hasil kunci:

```text
Kunci Publik : (p=467, g=2, y=58)
Kunci Privat: x=127
```

---

## Contoh Enkripsi

Misal pesan numerik `m = 123`
Bob memilih ephemeral key `k = 77`

Langkah perhitungan:

```text
a = g^k mod p = 2^77 mod 467 = 245
b = m * y^k mod p = 123 * 58^77 mod 467 = 398
```

Ciphertext: `(245, 398)`

---

## Representasi Cipher ASCII

Cipher dapat direpresentasikan sebagai **kode ASCII modulo 256**:

```python
cipher_ascii = [a % 256, b % 256]
```

Contoh:

```text
cipher = (245, 398)
cipher_ascii = [245 % 256, 398 % 256] = [245, 142]
```

> Nilai ini menunjukkan kode ASCII dari setiap byte cipher (tidak selalu printable).

---

## Contoh Dekripsi

Alice menerima cipher `(245, 398)`
Hitung shared secret:

```text
s = a^x mod p = 245^127 mod 467 = 333
```

Hitung invers modulo:

```text
s_inv = s^-1 mod p = 333^-1 mod 467 = 153
```

Dekripsi:

```text
m = b * s_inv mod p = 398 * 153 mod 467 = 123
```

ASCII 123 → pesan asli berhasil dipulihkan.

---

## Modular Exponentiation Langkah-demi-Langkah

Menghitung `a = g^k mod p` dengan **exponentiation cepat**:

| Pangkat | Perhitungan | Hasil mod p |
| ------- | ----------- | ----------- |
| 1       | 2           | 2           |
| 2       | 2^2         | 4           |
| 4       | 4^2         | 16          |
| 8       | 16^2        | 256         |
| 16      | 256^2       | 115         |
| ...     | ...         | ...         |
| 77      | ...         | 245         |

---

## Guidelines for contribution

* Fork repository ini
* Buat PR untuk perbaikan atau fitur baru
* Pastikan semua perubahan diuji secara lokal
