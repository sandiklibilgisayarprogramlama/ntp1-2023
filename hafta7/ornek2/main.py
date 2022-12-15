"""
Bir müzik grubunda 3 kişi bulunmaktadır. Bu üç kişiden ikisi
gitar çalmakta kalan 1 kişi ise davul çalmaktadır. Yaptıkları
müzikte nakarat kısmında gitarlar arka arkada 3 kez do notası,
5 kez mi notası çalarken davula 4 kez vurulmaktadır.
Bu işlemleri ekrana yazarak gerçekleştiren nesne tabanlı 
programlama örneğini gerçekleştiriniz.
"""

from gitarist import Gitarist
from davulcu import Davulcu
from muzik_grubu import MuzikGrubu

gitarist1 = Gitarist()
gitarist1.ad = "Emre"
gitarist1.gitar_turu = "Bas gitar"

gitarist2 = Gitarist()
gitarist2.ad = "Korhan"
gitarist2.gitar_turu = "Elektro gitar"

davulcu1 = Davulcu()
davulcu1.ad = "Yusuf"

grup = MuzikGrubu()
grup.ad = "Aşkı Müzik"
grup.gitarist1 = gitarist1
grup.gitarist2 = gitarist2
grup.davulcu = davulcu1

grup.gitarist1.nota_cal("Do", 3)
grup.gitarist2.nota_cal("mi", 5)
grup.davulcu.nota_cal(5)
