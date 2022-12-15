"""
docstring -> modülün ne işe yarıdıgınız özeti
"""
from otel import Otel
from oda import Oda
from kisi import Kisi


kisi_listesi = []
otel = Otel("Sandıklı Termal Otel")


def kisi_listesi_getir():
    if len(kisi_listesi) != 0:
        for kisi in kisi_listesi:
            print("tcno: "+kisi.tcno)
            print("Tam Ad: "+kisi.ad + " " + kisi.soyad)
            print("Tel ve adres: "+kisi.tel + " "+kisi.adres)
    else:
        print("Sistemde kisi bulunmuyor")


def oda_listesi_getir():
    if len(otel.oda_liste) != 0:
        for oda in otel.oda_liste:
            print("Oda no: "+oda.odano)
            print("Oda Gun Sayısı: "+str(oda.gun))
            print("Oda Günlük Ücreti: "+str(oda.gunluk_ucret))
    else:
        print("Sistemde oda bulunmuyor")


while True:
    print(
        otel.otel_ad+""" Otomasyonuna Hoşgeldiniz.
Devam etmek için ilgili kodu giriniz:
1- Kişi Ekle
2- Oda Ekle
3- Kişi Listesi
4- Oda Listesi
5- Odaya Kişi ekle
6- otel kisi liste
7- Çıkış
        """
    )
    girilen_kod = int(input("Menu Kodu Giriniz:"))
    if girilen_kod == 1:
        print("Kişi Ekle")
        kisi1 = Kisi(input("Tcno Giriniz: "), input("Ad giriniz: "), input(
            "Soyad giriniz: "), input("telefon giriniz: "), input("Adres giriniz: "))
        kisi_listesi.append(kisi1)
        print("Kisi eklendi")
    elif girilen_kod == 2:
        print("Oda ekle")
        oda = Oda(input("Oda no giriniz"), int(input("gün sayı giriniz")),
                  int(input("günlük oda ücretiniz giriniz")))
        otel.oda_liste.append(oda)
        print("Oda eklendi")
    elif girilen_kod == 3:
        print("Kisi Listesi: ")
        kisi_listesi_getir()

    elif girilen_kod == 4:
        print("Oda Listesi: ")
        oda_listesi_getir()

    elif girilen_kod == 5:
        print("Odaya Kişi Ekle")
        oda_listesi_getir()
        print("Kişi eklemek istediğiniz odayı seçiniz (oda no yazınız)")
        oda_no = input("Oda No giriniz")
        oda = None
        for index in range(len(otel.oda_liste)):
            if otel.oda_liste[index].odano == oda_no:
                oda = otel.oda_liste[index]
                break
        kisi_listesi_getir()
        print("Eklemek istediğiniz kişiyi seçiniz (tcno )")
        tcno = input("tc no giriniz")
        for kisi in kisi_listesi:
            if kisi.tcno == tcno:
                oda.kisi_liste.append(kisi)
        print("Kişi odaya eklendi")
    elif girilen_kod == 6:
        print("Otel Oda ve Kişi Listesi")
        for oda in otel.oda_liste:
            print("Oda no: "+oda.odano)
            print("Konaklayan:" +
                  oda.kisi_liste[0].ad+" "+oda.kisi_liste[0].soyad)
            print("----------------------------")
    elif girilen_kod == 7:
        print("Program Sonlandı")
        break
