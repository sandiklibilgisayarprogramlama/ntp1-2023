"""def isim(params):
    yapılacak_is
    return


Bir str ifade kabul eden ve büyük harf ve 
küçük harf sayısını hesaplayan bir Python fonksiyonunu yazın.
örnek: 'The quick Brow Fox'
büyük karakter sayısı : 3
küçük karakter sayısı : 12

"""


def buyuk_kuyuk_say_hesapla(metin):
    buyuk_say = 0
    kucuk_say = 0
    for harf in metin:
        if (harf == harf.upper()):
            # (ord(harf) < 96):  # harf.isupper()
            buyuk_say = buyuk_say+1
        else:
            kucuk_say = kucuk_say+1
    print("buyuk sayısı: "+str(buyuk_say))
    print("kucuk sayısı: "+str(kucuk_say))


buyuk_kuyuk_say_hesapla("eMrEEEeee")
"""
parametre olarak verilen bir kelimenin duz ve ters yazıldığında 
aynı olup olmadığını kontrol eden fonksiyonu yazınız.

parametre :
madam
mum
ada
ece
kayak


# kelimeyi tersine ceviren fonksiyon


def reverse(metin):
    ters_kelime = ""
    for index in range(len(metin)-1, -1, -1):
        ters_kelime = ters_kelime + metin[index]
    return ters_kelime


def palindrom(metin):
    if metin == reverse(metin):
        return True
    else:
        return False


print(palindrom("madam"))
print(palindrom("süleyman"))


mükemmel numara 
kendinden önceki tam bölenlerinin toplamı kendine eşitse
mükemmel
"""


def mukemmel_kontrol(sayi):
    tam_bolenler = []
    for k in range(1, sayi):
        if sayi % k == 0:
            tam_bolenler.append(k)
    if sayi == sum(tam_bolenler):
        return True
    else:
        return False


print(mukemmel_kontrol(10))

# spagetti kod
