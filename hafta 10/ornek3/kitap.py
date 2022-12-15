from kisi import Kisi


class Kitap:

    def __init__(self, ad: str,  kisi: Kisi, sayfa_sayisi: int, cilt_sayisi: int) -> None:
        self.ad = ad
        self.kisi = kisi
        if self.kisi == None:
            self.durum = 0
        else:
            self.durum = 1

        self.sayfa_sayisi = sayfa_sayisi
        self.cilt_sayisi = cilt_sayisi
