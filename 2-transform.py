print("==== Transform string uppercase / lowercase")
kata1 = 'javascript'
kata2 = 'JAVASCRIPT'
print(kata1.upper())
print(kata1.lower())

print("==== Awalan dan akhiran ====")
print("python    ".rstrip()) # menghapus spasi sebelah kanan
print("     python".lstrip()) # menghapus spasi sebelah kiri
print("     python     ".strip()) # menghapus spasi sebelah kiri & kanan
print("python adalah bahasa".rstrip("bahasa")) # python adalah
print("python adalah bahasa".lstrip("python ")) # adalah bahasa

print("===== Mencari nilai pada suatu string =====")
print("Python Language".startswith("Python")) # True
print("Python Language".startswith("JAVASCRIPT")) # False
print("Python Language".endswith("Language")) # True

print("==== Menggabung string ====")
print(' '.join(["indonesia", "raya"])) # indonesia raya
print('dan'.join(["mobil", "motor"]))

print("==== Memisahkan string ====")
print('Dicoding Indonesia !'.split()) # ['Dicoding','Indonesia','!']
print('Python diciptakan pada tahun 1991'.split())

print("==== Replace string ====") # case sensitive
string = "Ayo belajar Coding di Dicoding"
print(string.replace("Coding", "Pemrograman"))

print("===== Pengecekan string =====")
# cek apakah string uppercase / lowercase
lang = "PYTHON"
js = "JAVASCRIPt"
print(lang.isupper()) # True
print(lang.islower()) # False
print(js.isupper()) # false
# cek apakah isi variabel merupakan alfabet / bukan
alfabet1 = "ABC"
alfabet2 = "ABC24"
print(alfabet1.isalpha()) # True
print(alfabet2.isalpha()) # false

print("===== Pengecekan numerik =====")
number = '123'
charNum = 'john123'
char = 'john'
print(number.isalnum()) # True
print(charNum.isalnum()) # True
print(char.isalnum()) # True

print("===== Pengecekan huruf capital =====")
print('Python Language'.istitle()) # True
print('python Language'.istitle()) # false
