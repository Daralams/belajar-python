"""
TODO:
Buatlah sebuah fungsi bernama "minimal" dengan ketentuan berikut.
- Menerima dua buah argumen berupa number, yaitu a dan b.
- Mengembalikan nilai terkecil antara a atau b.
- Bila nilai keduanya sama, kembalikan dengan nilai a.
"""

# TODO: Silakan buat kode Anda di bawah ini.

def minimal(a, b):
  terkecil = min(a, b)
  if(a == b):
    return a
  return terkecil
  
print(minimal(10, 15))
print(minimal(10, 10))
  