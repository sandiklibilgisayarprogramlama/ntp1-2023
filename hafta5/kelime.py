"""
+* parametre olarak verilen cümledeki boşluk sayısını bulan fonk
+* parametre olarak verilen bir cümledeki harf sayısını bulan fonk
* parametre olarak verilen cümledeki kelime sayısını bulan fonk
+* parametre olarak verilen cümledeki büyük harf sayısını bulan fonk
+* parametre olarak verilen cümledeki küçük harf sayısını bulan fonk
+* parametre olarak verilen cümledeki noktalama işaret sayısını bulan fonk
"""

from string import punctuation

cumle = """Lorem Ipsum has been the industry's standard dummy text ever 
since the 1500s, when an unknown printer took a galley of type and scrambled 
it to make a type specimen book."""


def bosluk_say_bul(kelime):
    say = 0
    for harf in kelime:
        if harf == " ":
            say = say+1
    return say


def buyuk_harf_hesapla(kelime):
    say = 0
    for harf in kelime:
        if harf.isupper():
            say = say+1
    return say


def kucuk_harf_hesapla(kelime):
    say = 0
    for harf in kelime:
        if harf.islower():
            say = say+1
    return say


def harf_sayisi_hesapla(kelime):
    say = 0
    for harf in kelime:
        if harf.isalpha():
            say = say+1
    return say


def noktalama_sayisi_hesapla(kelime):
    say = 0
    for harf in kelime:
        if harf in punctuation:
            say = say+1
    return say


def kelime_say_bul(kelime):
    return len(kelime.split(" "))

# büyük harfle başlayan kelime sayısını bulunuz.


def buyuk_harfle_baslayan_say_bul(cumle):
    kelime_list = cumle.split(" ")
    say = 0
    for kelime in kelime_list:
        if kelime[0].isupper():
            say = say+1
    return say


# içerinde noktalama işareti olan kelimeler hangileri bulan fonksiyon
def noktalama_isaretli_kelimeler(cumle):
    kelime_list = cumle.split(" ")
    for kelime in kelime_list:
        for harf in kelime:
            if harf in punctuation:
                print(kelime)
                break


print(kucuk_harf_hesapla(cumle))
print(harf_sayisi_hesapla(cumle))
print(noktalama_sayisi_hesapla(cumle))
print(kelime_say_bul(cumle))
print(buyuk_harfle_baslayan_say_bul(cumle))
noktalama_isaretli_kelimeler(cumle)
