from araba import Araba

ornek_araba = Araba(2020, "Mercedes")
# nesne tanımlama (ornek oluşturma)
# ornek oluşturarak metod çağırma
ornek_araba.marka_yazdir()

# Sınıf ismiyle metod çağırma
# sınıf metodu
print(ornek_araba.kapi_sayisi)
Araba.sinif_metodu()
print(Araba.kapi_sayisi)
Araba.kapi_sayisi_guncelle(4)
print(Araba.kapi_sayisi)
print(ornek_araba.kapi_sayisi)
Araba.static_metod()
print(Araba.google_adres())
