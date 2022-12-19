from karakter_tip import KarakterTip
from takim import Takim
from karakter import Karakter
from karsilasma import Karsilasma
sovalye = KarakterTip("Şovalye", 50, 3, 100)
okcu = KarakterTip("Okçu", 20, 2, 60)
mancinik = KarakterTip("Mancınık", 100, 1, 400)

sovalye1 = Karakter("Şovalye Ahmet", sovalye)
okcu1 = Karakter("Okçu Korhan", okcu)
mancinik1 = Karakter("Mancinik Tolga", mancinik)
sovalye2 = Karakter("Şovalye Emre", sovalye)
okcu2 = Karakter("Okçu mert", okcu)
mancinik2 = Karakter("Mancinik ahmet", mancinik)
okcu3 = Karakter("Okçu yusuf", okcu)
mancinik3 = Karakter("Mancinik kubilay", mancinik)

takim1 = Takim([sovalye1, okcu1, mancinik1, sovalye2])
takim2 = Takim([okcu2, mancinik2, okcu3, mancinik3])

print("Takim 1 can : {}".format(takim1.can))
print("Takim 2 can : {}".format(takim2.can))
Karsilasma([takim1, takim2]).savas_basla()
