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