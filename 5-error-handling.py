z = 0
try:
  print(1/z)
except ZeroDivisionError:
  print("Gabisa membagi angka 0!")
  
print("==============================")

items = [0, 1, 2, 3, 4, 5, 6, 7]
for item in items:
  try:
    if item == 7:
      print("Angka tidak ditemukan!")
      break
  except:
      print("Angka tidak ada yg bertipe string")
  else:
    print(item)
  finally:
    print("Finished.....")
    
i = 9 
if i<10:    
    print(i) 
    
for i in range(1, 3):    
    for j in range(1, 3):    
    print(i,j) 
    