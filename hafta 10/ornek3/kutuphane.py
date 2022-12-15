class Kutuphane:
    def __init__(self, kitap_listesi: list, ad: str, adres: str, tel: str) -> None:
        self.ad = ad
        self.kitap_listesi = kitap_listesi
        self.adres = adres
        self.tel = tel

    def kutuphanede_bulunanlari_yazdir(self):
        for kitap in self.kitap_listesi:
            if kitap.durum == 0:
                print(kitap.ad)

    def tcnoya_gore_kitap_bilgisi(self, tcno):
        for kitap in self.kitap_listesi:
            if kitap.durum == 1:
                if kitap.kisi.tcno == tcno:
                    print(kitap.ad)
                    break

    def kitap_ada_gore_kisi_getir(self, kitap_ad):
        for kitap in self.kitap_listesi:
            if kitap.ad == kitap_ad:
                print(kitap.kisi.ad+" "+kitap.kisi.soyad)
