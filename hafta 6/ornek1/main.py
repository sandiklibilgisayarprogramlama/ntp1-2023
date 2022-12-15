from kullanici import *
from araba import *

araba1 = Araba()  # araba tipinde bir değişken

araba1.aylik_fiyat = 12000
araba1.beygir = 90
araba1.depo_buyuklugu = 40
araba1.gunluk_fiyat = 800
araba1.km_basina_yakit = 1.2
araba1.marka = "Fiat"
araba1.model = 2020
araba1.yakit_tipi = "Benzin"


kullanici1 = Kullanici()  # kullanici tipinde
kullanici1.ad = "Süleyman"
kullanici1.soyad = "Uzun"
kullanici1.cinsiyet = "E"
kullanici1.tcno = "123123131424"
kullanici1.kredi_kart_no = "4343432233434"
kullanici1.arac = araba1


print(kullanici1.ad)
print(kullanici1.arac.marka)
print(kullanici1.arac.model)
print(kullanici1.arac.beygir)
