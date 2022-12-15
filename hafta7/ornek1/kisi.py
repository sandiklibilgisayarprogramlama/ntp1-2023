"""
sinif vurgusu (self) sınıf içinde tanımlanan değişken 
yada fonksiyonların tekrardan sınıf içinde kullanılmak
istendiğin tanımlanması gereken bir parametredir.
Amacı öğelerin sınıfa ait olduğunu göstermektir.
"""
"""
sınıf değişkeni:
sınıf vurgusu (self) le birlikte sınıftaki tüm fonksiyonlarda
kullanılabilir.

fonksiyon değişkeni:
sadece tanımlandıgı fonksiyon içinde geçerlidir. Başka bir 
fonksiyonda kullanılamaz.

"""


class Kisi:
    ad = None  # sınıf değişkeni
    soyad = None
    dogum_yili = None
    uyruk = "TR"
    tc_no = None

    def ad_soyad_yazdir(self):
        print(self.ad+" "+self.soyad)

    def tum_bilgileri_yazdir(self):
        self.ad_soyad_yazdir()
        print(self.tc_no)
        print(self.uyruk)
        print(self.dogum_yili)

    # yıla göre yas hesapla
    def yila_gore_yas_hesapla(self, bulunulan_yil):
        print(str(bulunulan_yil) + " yılında yaş:")
        print(bulunulan_yil-self.dogum_yili)
