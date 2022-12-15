class Ogrenci:
    # değişkenler

    def __init__(self, ad, soyad, yas):
        self.ad = ad
        self.soyad = soyad
        self.yas = yas
        print("kurucu metod çalıştı")

    # metodlar

    def adYazdir(self):
        # ad = "ahmet"  # local değişken

        print(self.ad)
