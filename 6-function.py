print("===== PERSEGI PANJANG =======")
def luas_persegi_panjang(panjang, lebar):
  hasil = panjang * lebar
  return hasil

# Positional Argument 
persegi_panjang1 = luas_persegi_panjang(10, 15)
print(f'Hasil : ',persegi_panjang1)

persegi_panjang2 = luas_persegi_panjang(20, 15)
print(f'Hasil : ',persegi_panjang2)
# keyword argumen (mendefinisikan argumen menggunakan parameter)
persegi_panjang3 = luas_persegi_panjang(panjang=25, lebar=8)
print(f'Hasil : ',persegi_panjang3)

print("===== FUNGSI FX =======")
def fx(angka):
  hasil = angka * 2
  return hasil 
  
operasi1 = fx(2)
print(operasi1)

print("======= Fungsi cetak ===========")
def cetak(key):
  print(key)
  return 

cetak("Hello world")
cetak(250)

print("======= Fungsi mencari length ===========")
def panjang_karakter(karakter):
  print(len(karakter))
  return

panjang_karakter('Python programming')
panjang_karakter([1, 2, 3, 4])

"""
Var-Positional (Variadic Positional Parameter)
Parameter ini menampung jumlah argumen posisi yang bervariasi saat pemanggilan fungsi.
"""

def total(*args): 
  print(args)
  print(type(args))
  print(sum(args))
  print(len(args))
  print(max(args))
  return 

total(1, 2, 3, 4, 5, 6)
total(8 ,7 ,6, 5, 4, 3, 2,1)

def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info

print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))
"""
Output:
nama: Dicoding, usia: 17, pekerjaan: Python Programmer,
"""

print("===== Fungsi lamda (anonym function) ======")
luasPersegiPanjang = lambda panjang, lebar: panjang * lebar

print(luasPersegiPanjang(12, 3))
