from araba import Araba
from aracservis import AracServis
arac = Araba("mercedes", 2013, 90, "dizel")
arac.model_yazdir()
print(arac.marka_dondur())

arac2 = Araba("fiat", 2020, 80, "benzin")
arac2.model_yazdir()
print(arac2.marka_dondur())

arac_servis = AracServis([arac, arac2])
