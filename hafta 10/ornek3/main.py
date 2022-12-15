from kisi import Kisi
from kutuphane import Kutuphane
from kitap import Kitap

kisi1 = Kisi("yusuf", "uzun", 53467467467, "14342342423", "merkez sandıklı")
kisi2 = Kisi("ahmet", "yılmaz", 5344367890, "23645779922", "merkez sandıklı")
kisi3 = Kisi("emre", "mor", 5123323543, "890043242342", "merkez sandıklı")
kisi4 = Kisi("yılmaz", "mor", 5123323435, "23432279922", "merkez sandıklı")

kitap1 = Kitap("Suç ve Ceza", kisi1, 400, 2)
kitap2 = Kitap("Fareler ve İnsanlar", None, 200, 1)
kitap3 = Kitap("Simyacı", kisi3, 140, 1)
kitap4 = Kitap("Uçurtma Avcısı", kisi4, 500, 1)

kutuphane = Kutuphane([kitap1, kitap2, kitap3, kitap4], "Sandıklı Merkez Küt.",
                      "Merkez sandıklı", "02723234422")

kutuphane.kutuphanede_bulunanlari_yazdir()
kutuphane.tcnoya_gore_kitap_bilgisi("23432279922")
kutuphane.kitap_ada_gore_kisi_getir("Simyacı")
