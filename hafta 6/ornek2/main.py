from yiyecek import Yiyecek
from icecek import Icecek
from market import Market

y1 = Yiyecek()
y1.ad = "Bisküvi"
y1.ucret = 20
y1.son_kullanma_tarihi = "12.12.2022"

y2 = Yiyecek()
y2.ad = "Kraker"
y2.ucret = 10
y2.son_kullanma_tarihi = "12.12.2022"


i1 = Icecek()
i1.ad = "Süt"
i1.ucret = 12
i1.son_kullanma_tarihi = "12.12.2022"

market1 = Market()
market1.icecekler = i1
market1.yiyecekler = [y1, y2]
market1.ad = "Süper Market"
market1.adres = "Afyon"

market1.yiyecekleri_yazdir()

# marketteki yiyecekleri ekrana yazdıracak fonksiyonu yazalım.
# marketteki icecekleri ekrana yazdıracak fonksiyon
# markette toplamda kaç adet yiyecek ve icecek oldugunu
# ekrana yazan fonksiyon
market1.icecekleri_yazdir()
print(market1.stok_miktar())
