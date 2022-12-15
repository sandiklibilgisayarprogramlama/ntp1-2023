"""
sinif vurgusu (self) sınıf içinde tanımlanan değişken 
yada fonksiyonların tekrardan sınıf içinde kullanılmak
istendiğin tanımlanması gereken bir parametredir.
Amacı öğelerin sınıfa ait olduğunu göstermektir.
"""

class Market:
    ad: None
    yiyecekler = None
    icecekler = None
    adres = None

    def yiyecekleri_yazdir(self):
        for yiyecek in self.yiyecekler:
            print(yiyecek.ad, end=" - ")
            print(yiyecek.ucret, end=" - ")
            print(yiyecek.son_kullanma_tarihi)

    def icecekleri_yazdir(self):
        print("---------İcecekler------------")
        print(self.icecekler.ad, end=" - ")
        print(self.icecekler.ucret, end=" - ")
        print(self.icecekler.son_kullanma_tarihi)

    def stok_miktar(self):
        return len(self.yiyecekler)+1
