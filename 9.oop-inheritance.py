class Atlet_lari:
  def __init__(self, nama, kelincahan, kecepatan):
    self.nama = nama
    self.kelincahan = kelincahan
    self.kecepatan = kecepatan
    
  def tambah_kecepatan(self):
    for i in range(self.kecepatan + 11):
      nilai_kecepatan = []
      nilai_kecepatan.append(i)
      akumulasi = sum(nilai_kecepatan)
      kecepatan_akhir = self.kecepatan = akumulasi
      
      
# inheritance / pewarisan dari class Atlet_lari
class Petinju(Atlet_lari):
  """def __init__(self, power):
    self.power = power """
  def intro(self):
    print(f'Intro : Hello my name is ', self.nama, ' im a boxer, with speed ', self.kecepatan, ' and agility ', self.kelincahan)
    
  # super method untuk memanggil method tertentu tanpa Override
  def tambah_kecepatan(self):
    super().tambah_kecepatan()
    print(f'Kecepatan anda meningkat menjadi : ', self.kecepatan, self.nama, ', manfaatkan kecepatan anda pada ronde berikutnya!')
      
atletLari1 = Atlet_lari('John doe', 'diatas rata rata', 20)
print("===== Kecepatan awal =======")
print("Atlet lari : ")
print(f'Nama : ', atletLari1.nama)
print(f'Tingkat kelincahan : ', atletLari1.kelincahan)
print(f'Kecepatan awal : ', atletLari1.kecepatan)

atletLari1.tambah_kecepatan()
print("===== Kecepatan maksimal =======")
print(f'Nama : ', atletLari1.nama)
print(f'Tingkat kelincahan : ', atletLari1.kelincahan)
print(f'Kecepatan maksimal : ', atletLari1.kecepatan)

print("Petinju : ")
petinju1 = Petinju('Ryan garcia', 'diatas rata rata', 250)
#print(f'Power : ', petinju1.power)
print(f'Nama : ', petinju1.nama)
print(f'Tingkat kelincahan : ', petinju1.kelincahan)
print(f'Kecepatan maksimal : ', petinju1.kecepatan)
petinju1.intro()
petinju1.tambah_kecepatan()