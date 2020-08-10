import random
import string

#Giriş
#chars uzunluğu 94 elemandan oluşuyor yani 93 index'i var

char_len=int(input("Lütfen şifrenizin uzunluğunu giriniz!(4-12):"))
while char_len > 12 or char_len < 4:
    char_len=int(input("Lütfen geçerli bir değer giriniz(4-12):"))

#Karakterlerin tanımı

chars=string.ascii_letters+string.punctuation+string.digits
password=""

#Şifre oluşturma

for c in range(char_len):
 password += chars[random.randint(0,93)]

#Şifreyi ekrana yazdırma

shuffled_pass=''.join(random.sample(password,len(password)))
print("Şifreniz oluşturuldu:"+" "+password)
print("Şifrenizin farklı bir dizilimi:"+" "+shuffled_pass)


#Uzun yol(Long Way)
"""
#Giriş ve şifre uzunluğu değişkeni
print("Rastgele şifre oluşturucuya hoşgeldiniz!")
char_length=3               #For döngüsü nedeni ile 1 döngüde 4 karakter oluşturacak 12 karakterli bir şifre oluşturmak için 3 değerini veriyoruz.

#Karakterler
char_upper=list(string.ascii_uppercase)
char_lower=list(string.ascii_lowercase)
char_nums=list(string.digits)
another=list(string.punctuation)

#Şifre değişkenimiz
password=""

#Rastgele karakter seçerek şifre oluşturmak
for i in range(char_length):
     one=char_upper[random.randint(0,25)]

     two=char_lower[random.randint(0,25)]

     three=char_nums[random.randint(0,9)]

     four=another[random.randint(0,31)]

     password +=one+two+three+four

#Oluşturulan şifreyi yazdırmak
print("\n")
shuffled_password="".join(random.sample(password,len(password)))
print("Tebrikler yeni Şifreniz:"+" "+password)
print("Şifrenizin farklı bir dizilimi:"+" "+shuffled_password)
"""

