class Araba:
    kapi_sayisi = 0

    def __init__(self, model, marka):
        self.model = model
        self.marka = marka

    def marka_yazdir(self):
        print(self.marka)

    # def metod_adi(sinif_belirteci):
    #    pass

    def ornek_metodu(self):
        print("ornek metodu")

    @classmethod  # annotation
    def sinif_metodu(cls):
        print("sinif metodu")

    @classmethod
    def kapi_sayisi_guncelle(cls, kapi_sayisi):
        cls.kapi_sayisi = kapi_sayisi

    # static metodlar
    @staticmethod
    def static_metod():
        print("static metod")

    @staticmethod
    def google_adres():
        return "https://www.google.com"
