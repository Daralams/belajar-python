import re # import regex

pola = '^b...s$' 
"""
pola harus memiliki huruf depan 'b', angka di tengah sebanyak 3 karakter dan akhiran huruf s
"""
text = 'bishs'
result = re.match(pola, text)

if (result):
  print('match')
else:
  print('not match')
  
print("==== Email validation =====")

pattern = r"\@\.com$"
email = 'example@gmail.com'
email_check = re.search(pattern, email)

if(email_check):
  print(f'{email}, This email valid')
else:
  print(f'{email}, This email is not valid')