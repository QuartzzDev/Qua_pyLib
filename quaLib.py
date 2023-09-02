################################
# QuartzzDev <3    quartzz.dll #
################################




################################
# Gerekliler                   #
################################ 

import math
import random
import pyfiglet
import pytz
from colorama import init, Fore, Back, Style
init(autoreset=True)






###############################
# Matematiksel Fonsiyonlar    #
###############################

def Topla(a,b):                     # 2 sayıyı toplamak için
    print(a+b)

def Cikart(a,b):                    # 2 sayıyı Çıkartmak için
    print(a-b)

def Carp(a,b):                      # 2 sayıyı Çarpmak için
    print(a*b)

def Bol(a,b):                       # 2 sayıyı Bölmek için
    print(a/b)

def ussuAl(a,b):                    # Sayının üssünü almak için
    print(a,"Üzeri",b,":",a**b)

def kupAl(a):                       # Sayının küpünü almak için
    kup = math.pow(a, 3)
    print(a,"'nın Küpü :",kup)

def kupHacim(a):                    # Bir küpün hacmini bulmak için
    print("Küpün Hacmi :",a*a*a)

def kareAlan(a,b):                  # Bir karenin alanı bulmak için
    print("Karenin Alanı :",a*b)

def daireAlan(r):                   # Bir dairenin alanı bulmak için
    print("Yarıçapı",r,"Olan Dairenin Alanı :",math.pi * r ** 2)

def silindirAlan(uzunluk,yukseklik,r):  # Bir silindirin alanı bulmak için
    silindir = (math.pi * r ** 2) * 2 + uzunluk*yukseklik
    print("Silindirin Alanı :",silindir)  
    
def silindirHacim(yukseklik,r):
    print((math.pi * r ** 2) * yukseklik)   # Bir silindirin hacmini bulmak için

def pisagor(a, b):                          
    c = (a**2 + b**2) ** 0.5
    print(c)

def asalMi(sayi):                       # Bir sayi/rakam'ın asal olup olmadığını bulmak içinZ
    if sayi <= 1:
        print(f"{sayi} asal bir sayı değildir.")
    for i in range(2, int(sayi**0.5) + 1):
        if sayi % i == 0:
            print(f"{sayi} asal bir sayı değildir.")
            break
    else:
        print(f"{sayi} asal bir sayıdır.")






###############################
# Kullanıcıdan Veri Alma      #
###############################

def InputAlStr(metin):          # Kullanıcıdan String Değer Almak İçin
    yazi = input(metin)

def InputAlInt(metin):          # Kullanıcıdan Int Değer Almak İçin
    yazi = int(input(metin))

def InputAlFloat(metin):        # Kullanıcıdan Float Değer Almak İçin
    yazi = float(input(metin))

def IstekMetinYazdir(metinSayi, metin):     # Kullanıcının istediği bir metni , istediği kadar yazdırmasını sağlamak için
    metinSayi = int(metinSayi)
    for _ in range(metinSayi):
        print(metin)

def text_3d(text):                # Kullanıcının istediği bir metni , 3D bir şekilde yazmak için
    custom_fig = pyfiglet.Figlet(font='slant')
    ascii_text = custom_fig.renderText(text)
    print(ascii_text)



def analyze_data(data):         # Kullanıcıdan gelen verilerin analiz edilmesini sağlamak için
    if len(data) == 0:
        return None

    total = sum(data)
    average = total / len(data)
    max_value = max(data)

    analysis = {
        "count": len(data),
        "total": total,
        "average": average,
        "max": max_value
    }

    return analysis

""" Bu kod örneği, elinizde bulunan verileri nasıl analiz edebileceğinizi gösteren bir örnektir.

data_list = [23, 45, 12, 67, 89, 34, 56, 78, 98, 22]
result = analyze_data(data_list)

if result:
    print("Veri Analizi Sonuçları:")
    print(f"Toplam Veri Sayısı: {result['count']}")
    print(f"Toplam Değer: {result['total']}")
    print(f"Ortalama Değer: {result['average']:.2f}")
    print(f"En Büyük Değer: {result['max']}")
else:
    print("Veri bulunamadı")
"""






###############################
# Renkli Printler             #
###############################

def RedPrint(metin):
    print(Fore.RED + metin)       # Kırmızı yazı yazdırmak için
    print(Style.RESET_ALL)

def BluePrint(metin):
    print(Fore.BLUE + metin)       # Mavi yazı yazdırmak için
    print(Style.RESET_ALL)

def YellowPrint(metin):
    print(Fore.YELLOW + metin)       # Sarı yazı yazdırmak için
    print(Style.RESET_ALL)

def CyanPrint(metin):
    print(Fore.CYAN + metin)       # Camgöbeği yazı yazdırmak için
    print(Style.RESET_ALL)

def WhitePrint(metin):
    print(Fore.WHITE +metin)       # Beyaz yazı yazdırmak için
    print(Style.RESET_ALL)

def MagentaPrint(metin):
    print(Fore.MAGENTA + metin)       # Magenta renkte yazı yazdırmak için
    print(Style.RESET_ALL)

def JustPrint(metin):               # Sadece yazı yazdırmak için
    print(metin)






###############################
# Random Seçimler             #
############################### 

def RandomList():               # Kullanıcıdan aldığımız verileri bir liste atıp , içinden rastgele seçtirmek için
    newList = []
    i = 1
    while i > 0:
        listMetin = input("Listeye Eklemek İstediğiniz Kelime/Cümleyi Girin : ")
        newList.append(listMetin)

        soru = input("Devam (D) , Çıkış (C) : ")
        if soru.lower()  == "d":
            i = 1
        elif soru.lower()  == "c":
            i = 0
        else:
            print("Yanlış Giriş Yaptınız.")
            i = 1
    else:
        rastgeleSec = random.choice(newList)
        print(rastgeleSec)


def CreateList():               # Kullanıcının verdiği verilere göre bir list oluşturup bu listeyi yine kullacının verdiği veriler ile doldurmak için 
    listName = input("Listenin ismi ne olacak ? ")
    listName = []
    i = 1
    while i > 0:
        newText = input("Listenize eklemek istediğiniz veriyi girin : ")
        listName.append(newText)

        soru = input("Devam (D) , Çıkış (C) : ")
        if soru.lower() == "d":
            i = 1
        elif soru.lower() == "c":
            i = 0
        else:
            print("Yanlış Giriş Yaptınız.")
            i = 1
    else:
        print("Listeniz\n",listName,"\n")
        print("Listeniz Kaydedildi .")






###############################
# Dosya Veri Alışverişi       #
############################### 

def dosyaya_yazdir(dosya_adi, metin):           
    try:
        with open(dosya_adi, 'w') as dosya:
            dosya.write(metin)
        print("Metin dosyaya yazıldı.")
    except Exception as e:
        print("Hata:", e)

def dosyadan_sil(dosya_adi):
    try:
        with open(dosya_adi, 'w') as dosya:
            dosya.write('')
        print("Dosya içeriği silindi.")
    except Exception as e:
        print("Hata:", e)

def karakter_sayisi(dosya_adi):
    try:
        with open(dosya_adi, 'r') as dosya:
            metin = dosya.read()
            sayi = len(metin)
        print(f"Toplam karakter sayısı: {sayi}")
    except Exception as e:
        print("Hata:", e)

def dosya_adi_degistir(eski_dosya_adi, yeni_dosya_adi):
    try:
        import os
        os.rename(eski_dosya_adi, yeni_dosya_adi)
        print("Dosya adı değiştirildi.")
    except Exception as e:
        print("Hata:", e)

def txtOlustur(dosya_adi):
    with open(dosya_adi, "w") as dosya:
        print("Dosya Oluşturuldu . .")

def dosya_icerigi_oku(dosya_adi):
    try:
        with open(dosya_adi, 'r') as dosya:
            icerik = dosya.read()
        print("Dosya İçeriği:")
        print(icerik)
    except Exception as e:
        print("Hata:", e)

def dosya_sonuna_ekle(dosya_adi, metin):
    try:
        with open(dosya_adi, 'a') as dosya:
            dosya.write(metin)
        print("Metin dosyanın sonuna eklendi.")
    except Exception as e:
        print("Hata:", e)

def dosya_kopyala(kaynak_dosya, hedef_dosya):
    try:
        with open(kaynak_dosya, 'r') as kaynak, open(hedef_dosya, 'w') as hedef:
            icerik = kaynak.read()
            hedef.write(icerik)
        print("Dosya kopyalandı.")
    except Exception as e:
        print("Hata:", e)






###############################
# Diğer                       #
############################### 

def buyukKucuk(sentence):           # Yazdığınız veriyi bir büyük bir küçük yazar.
    new_sentence = ""               
    to_upper = True 

    for char in sentence:
        if char.isalpha():
            if to_upper:
                new_sentence += char.upper()
            else:
                new_sentence += char.lower()
            to_upper = not to_upper
        else:
            new_sentence += char
    
    print(new_sentence)


def listeCevir(list):          # Listenizi Ters Çevirir
    print(list[::-1])          


def tekrarBul(list):            # Listenizde tekrarlayan ifadeleri bulur
    seen = {}                    
    duplicates = []
    for item in list:
        if item in seen:
            if item not in duplicates:
                duplicates.append(item)
        else:
            seen[item] = 1
    print(duplicates)


def tersYaz(text):              # Girdiğiniz yazıyı tersten yazar
    print(text[::-1])           

    
def uzunuBul(sentence): # Girdiğiniz cümledeki en uzun kelimeyi bulur
    words = sentence.split()
    longest_word = max(words, key=len)
    print("En uzun kelime:", longest_word)


def celtofah(celsius):      # Santigrat -> Fahrenheit
    fahrenheit = (celsius * 9/5) + 32
    print(fahrenheit)


def fahtocel(fahrenheit):   # Fahrenheit -> Santigrat
    celsius = (fahrenheit - 32) * 5/9
    print(celsius)


def listeBirlestir(list1, list2):  # 2 listeyi birleştirmeye yarar
    birlestirilmisListe = list1 + list2
    print(birlestirilmisListe)


def tekrarSil(list):   # Listelerde tekrarlayan verileri silerek yeni bir liste yapar
    unique_list = []
    for item in list:
        if item not in unique_list:
            unique_list.append(item)
    print(unique_list)


def analyze_file(file_path):            # Verdiğiniz dosyayı analiz eder
    with open(file_path, "r") as file:
        text = file.read()
        char_count = len(text)
        word_count = len(text.split())
        unique_words = len(set(text.split()))
        avg_word_length = sum(len(word) for word in text.split()) / word_count
    return {
        "Karakter Sayısı": char_count,
        "Kelime Sayısı": word_count,
        "Benzersiz Kelime Sayısı": unique_words,
        "Ortalama Kelime Uzunluğu": avg_word_length
    }



