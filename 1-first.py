# var assigment
nama = 'john'
print('Hello bro ' + nama)

angka = 1
result = angka + 5
print(result)

# input 
print("======== Form ========")
yourName = input("What is your name? : ")
print(f"Hello {yourName}")
print("======================")

# komentar 1 line
"""
komentar multiline
"""

angka = 20
char = 'hello'
print(type(angka))
print(type(char))

# Data types 
print("====== Primitif Data types (single value) ======")
"""
Dalam Python, tipe data dikelompokkan
menjadi dua, yakni tipe data primitif dan
tipe data collection.
"""
# type data primitif (single value)
type1 = 20 #int
type2 = 3.14 #float
type3 = 1+2j #complex
type4 = True #boolean
type5 = False #boolean
type6 = "string" #string
strMultiLine = """ 
tanda kutip seperti ini 
digunakan untuk menyimpan 
nilai / value string yang
multi line
"""
print(type(type1))
print(type(type2))
print(type(type3))
print(type(type4))
print(type(type5))
print(type(type6))
print(strMultiLine)
print(strMultiLine[5]) #menampilkan index string ke 5
# methode slicing karakter 
print(strMultiLine[7:]) # mengambil nilai str karakter pada index ke 6, lalu menampilkannya hingga index terakhir

print("=== Coba menimpa nilai variabel ===")
var = 12
print(var)
var = 15
print(var)

cek = 20
print("Jawaban : {}".format(cek)) # format untuk menggabung string dengan integer

print("====== Collection Data types (multiple value) ======")
# list 
myList = [1, "john", True, 2.5, 1+2j]
myList[2] = False
print(myList)
print(myList[1]) # john
print(myList[2]) # False
print(myList[-1]) # 1+2j (mengakses index list 1 terakhir)
print(type(myList)) # class list

# slicing 
items = ["laptop", "mouse", "keyboard", "monitor", "pc"]
print(items[0:3:1]) # [laptop, monitor, mouse]

# tuple (sama seperti list, namun value dari tuple tdk bisa berubah)
myTuple = ("indonesia" , "malaysia", 10, True, 5.20, False)
print(myTuple)
print(myTuple[1])
# myTuple[1] = "brazil"
# print(myTuple[1]) # error
print(type(myTuple)) # class tuple

# set 
print("==== set =====")
mySet = {2, 3, 4, 2, 5, 10, 19, 25, 31}
print(mySet)
print(type(mySet))
# set tidak memiliki index, sehingga tdk bisa melakukan ini : 
# print(mySet[0]) # TypeError: 'set' object is not subscriptable
# set bersifat unik

multi = ["jarot", "mukmin", 20, {True, 20}, (1, 2, 3)]
print(multi)

# method union dan intersection
""" 
1. union -> penggabungan nilai 2 variabel (himpunan 2 buah variabel)
2. intersection -> irisan antar 2 variabel yang memiliki nilai yg sama 
"""
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6, 7, 8, 9, 10}
print("set 1 : ", set1)
print("set 2 : ", set2)
print("Setelah digabungkan dengan method union : ")
fUnion = set1.union(set2)
print("Union : ", fUnion)

print("Setelah di iris menggunakan method intersection : ")
fIntersection = set1.intersection(set2)
print("intersection : ", fIntersection)

print("==== dictionary ====")
# dictionary -> key : value (kek object di js)
myDict = {
  "firstname": "Ahmad",
  "middlename": "Notosastro",
  "lastname": "Husodo",
  "age": 36,
  "address": "jakarta pusat",
  "email": "ahmad1234@gmail.com"
}
myDict["phone"] = "0813645794642" # menambah data ke dict 
myDict["job"] = "arsitek"
del myDict["address"] # delete data address
myDict["age"] = 45 # merubah data age
print(myDict)
print(myDict["lastname"])
print(type(myDict)) # class dict

print("==== Konversi tipe data =====")
print(int("25"))
print(str(25))
print(float("25"))
print(str(25.6))
print(tuple([2, 3,1 ,12, 5]))
print(list("Python programming"))
myData = [["name", "ahmad"], ["age", 35]]
print(dict(myData))
print(dict([(3,26),(4,44)])) # {3:26, 4:44}

# angka1 = '1'
# angka1 += 2 
# print(angka1) # TypeError: can only concatenate str (not "int") to str