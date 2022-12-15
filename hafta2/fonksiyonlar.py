import random
"""
def fonksiyon_ismi(parametre):
    işlem
"""

# parametre olarak verilen iki sayınını toplamını
# ekrana yazan fonksiyon


def topla(a, b):
    c = a + b
    print(c)


#topla(1, 67)
#topla(30, 50)
#topla(-10, 30)
#topla(45, 56)

"""
def rastgele_topla():
    s1 = random.randint(0, 100)
    s2 = random.randint(0, 100)
    print(s1+s2)


rastgele_topla()
rastgele_topla()
rastgele_topla()
"""

"""
parametre olarak bir kelime ve bir tekrar sayısı alan
tekrar sayısı kadar ekrana kelimeyi yazan fonksiyonu 
yazınız.


def tekrarla(kelime, kelime2, tekrar_sayisi):
    for i in range(tekrar_sayisi):
        if i % 2 == 0:
            print(kelime)
        else:
            print(kelime2)


tekrarla("selam", "merhaba", 10)

#tekrarla("merhaba", 4)
"""


def cikarma(say1, say2):
    sonuc = say1-say2
    return sonuc


asd = cikarma(10, 2)
ss = asd + 1
print(ss)


"""
islem adlı bir fonksiyon tanımlayınız.
fonksiyon 3 parametre alacak.
sayi1
sayi2
islem_adi

eğer işlem adı toplam ise fonksiyon girilen 
sayi1 ve sayi2 değerlerini toplayacak

eğer işlem adı cikarma ise fonksiyon girilen
sayi1 ve sayi2 değerlerini çıkaracak

bölme ise bölecek, çarpma ise çarpacak.
bu işlemleri hesaplayacak kodu yazınız.

"""


def islem(s1, s2, islem_adi):
    if islem_adi == "toplam":
        print(s1+s2)
    elif islem_adi == "cikarma":
        print(s1-s2)
    elif islem_adi == "bolme":
        print(s1/s2)
    elif islem_adi == "carpma":
        print(s1*s2)


islem(12, 34, "carpma")

"""
parametre olarak verilen bir sayının asal olup
olmadığını bulan fonksiyonu yazınız.

10 
2,3,4,5,6,7,8,9

"""

"""
def asal_control(sayi):
    for k in range(2, sayi):
        if sayi % k == 0:
            return False

    return True


print(asal_control(15))
"""


"""
parametre olarak verilen ad ve soyad için
adın sadece ilk harfini büyük, soyadın ise hepsini büyük
hale getirip geriye döndüren fonksiyonu yazınız.
capitalize() -> ilk harfi büyüten
upper() -> hepsini büyüten
"""

"""
ÖDEV

parametre olarak girilen iki sayı arasındaki asal sayıları 
ekrana yazan
fonksiyonu yazınız.
"""


def formatla(ad, soyad):
    if (type(ad) != str or type(soyad) != str):
        return "Yanlış ifade girdiniz"
    return ad.capitalize() + " " + soyad.upper()


print(formatla("ahmet", -1000))

"""
fonksiyonlarda parametreler farklı sıralar ilede gönderilebilir.
"""

print(formatla(soyad="kısa", ad="mehmet"))
print(formatla(ad="mehmet", soyad="kısa"))
print(formatla("mehmet", "kısa"))

"""
fonksiyonlarda başlangıçta sayısı bilinmeyen
parametre verebilmek için * simgesinden yararlanılır.



def hepsiniCumledeBuyukYaz(*kelimeler):
    for k in kelimeler:
        print(k.upper(), end=" ")


hepsiniCumledeBuyukYaz("ahmet", "naber", "napıyorsun", "iyisin", "güzel")
print("")


def hepsiniCumledeBuyukYazListe(kelimeler):
    for k in kelimeler:
        print(k.upper(), end=" ")


hepsiniCumledeBuyukYazListe(
    ["ahmet", "naber", "napıyorsun", "iyisin", "güzel"])



Pythondaki sum fonksiyonun işlevini gerçekleştiren fonksiyonu yazınız.
liste=[1,2,3]
sum(liste)
"""


def hepsini_topla(liste):
    toplam = 0
    for sayi in liste:
        toplam = toplam+sayi
    return toplam


print(hepsini_topla([1, 2, 3, 4]))
print(sum([1, 2, 3, 4]))

"""
max - bir listedeki en yüksek sayısı bulan fonksiyon
maxın görevini yapan fonksiyonu yazınız.
"""


def en_buyuk_bul(liste):
    buyuk = liste[0]
    for k in liste:
        if k > buyuk:
            buyuk = k
    return buyuk


print(en_buyuk_bul([-80, -90, -12, -10, -1]))
print(max([-80, -90, -12, -10, -1]))

"""
ÖDEV
parametre olarak verilen listedeki en büyük 
ikinci sayısı bulan fonksiyonu yazınız
"""

"""
fonksiyona parametreleri isimleriyle vermek istediğimizde
** işaretinden yararlanılır.



def ad_soyad_yazdir(**p):
    print(p["ad"]+" "+p["soyad"])


ad_soyad_yazdir(ad="veli", soyad="uzun")


def ad_soyad_yazdir_sozluk(dic):
    print(dic["ad"]+" "+dic["soyad"])


ad_soyad_yazdir_sozluk({"ad": "veli", "soyad": "uzun"})


fonksiyonlarda default(ön tanımlı) parametre verilebilir.



def dogum_yeri_yaz(dogum_yeri="Afyon"):
    print("Doğum Yerim : ", dogum_yeri)


dogum_yeri_yaz("Isparta")
dogum_yeri_yaz("Ankara")
dogum_yeri_yaz()



parametre olarak verilen str ifadeyi ters çevirip ekrana yazdıran
fonksiyonu yazınız.
merhaba
abahrem

"""


def reverse(input="merhaba"):
    for index in range(len(input)-1, -1, -1):
        print(input[index], end="")
    print()


reverse()
reverse("mustafa")

"""
parametre olarak int bir sayı alan ve faktoriyelini 
geri döndüren fonksiyonu yazınız.

parametre olarak 1 sayı ve aralık değerleri alan
fonksiyon yazıp sayının o aralıkta olup olmadığını 
ekrana yazdırınız.
aralik_kontrol(sayi=10,baslangic=5,bitis=20)

Bir str ifade kabul eden ve büyük harf ve 
küçük harf sayısını hesaplayan bir Python fonksiyonunu yazın.
örnek: 'The quick Brow Fox'
büyük karakter sayısı : 3
küçük karakter sayısı : 12
"""


def faktoriyel(sayi):
    if (type(sayi) != int):
        return "Sayi girmeniz gerekli"

    sonuc = 1
    for k in range(1, sayi+1):
        sonuc = sonuc * k
    return sonuc


print(faktoriyel(4))  # 4*3*2*1
