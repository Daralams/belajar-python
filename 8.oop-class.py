print("==== Class ====")
class Car:
  color = "red"
  
car1 = Car()
print(car1.color) # red
# mengubah value properti
car1.color = 'blue'
print(car1.color) # blue


print("==== Class Constructor ====")
class Home:
  # Attribut instance
  def __init__(self):
    self.luas = '300 m²' # attribut diberikan nilai default
    
home1 = Home()
print(home1.luas) # 300 m²

home1.luas = '250 m²'
print(home1.luas)

class Motor:
  def __init__(self, warna, jenis, mesin):
    self.warna = warna
    self.jenis = jenis
    self.mesin = mesin 
    
motor1 = Motor('Hitam', 'Sport', '250cc')
print(motor1.warna)
print(motor1.jenis)
print(motor1.mesin)

print("==== Decorator ====")
""" 
Decorator adalah sebuah function pada py yanng memanggil function lain
"""
def parent(func):
  def child():
    print("sebelum di eksekusi...")
    func()
    print("setelah di eksekusi...")
  return child
  
@parent 
def sayGoodBye():
  print('Hello python...')

sayGoodBye() 


print("====== Method class =======")
class Pesawat:
  def __init__(self, jenis, bobot, kecepatan):
    self.jenis = jenis
    self.bobot = bobot
    self.kecepatan = kecepatan
    
  """
  static Method (sama seperti function
  biasa, tidak terikat oleh instance
  class, hanya saja didefinisikan didalam
  class) 
  """
  @staticmethod
  def kondisi():
    print("~ Kondisi pesawat baik, pesawat siap terbang...")
    
  @classmethod
  def persiapan(cls):
    print("~ Pesawat akan terbang dalam hitung mundur 1 menit...")
  
  def tambah_kecepatan(self):
      self.kecepatan += 15
      
  def berhenti(self):
    self.kecepatan = 0
    
      
Pesawat.kondisi() # pemanggilan method static tidak perlu membuat instance classnya
Pesawat.persiapan()
air_asia = Pesawat('Air asia', '100kg', 20)
print(f"Sebelum tambah kecepatan : ", air_asia.kecepatan)

air_asia.tambah_kecepatan()
print(f"Setelah tambah kecepatan : ", air_asia.kecepatan)

air_asia.berhenti()
print(f"Setelah berhenti, kecepatan : ", air_asia.kecepatan)
