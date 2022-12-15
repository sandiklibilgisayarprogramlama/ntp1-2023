"""
Araç kiralama sistemi

Araba

marka 
model
beygir
yakit_tipi
depo_buyuklugu
gunluk_fiyat
aylik_fiyat
km_basina_yakit

* bir haftada ne kadar kazanacağim goster (gunluk_fiyat * 7)
* ben günü gireyim bana ne kadar kazanacağım goster (kac_gun * gunluk_fiyat)
* aylik verdiysem fiyati hesapla
* temel bilgileri göster
* 100 km gidince ne kadar yakar 

class SinifAdi:
    # sinifin_özellikleri (attributes)

    # işlevler (functions)

"""


class Araba:
    marka = None
    model = None
    beygir = None
    yakit_tipi = None
    depo_buyuklugu = None
    gunluk_fiyat = None
    aylik_fiyat = None
    km_basina_yakit = None

    """
    Sinif içinde bir fonksiyon yazacaksak ilk parametre her zaman self yazılmalı
    """

    def haftalik_kazanc(self):
        return self.gunluk_fiyat*7
