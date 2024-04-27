a = 10 # global
def tambah(b):
  print(a + b)
  return

tambah(20) # 30

def kurang(c):
  d = 20 # local
  print(c - d)
  return

kurang(15) # -5