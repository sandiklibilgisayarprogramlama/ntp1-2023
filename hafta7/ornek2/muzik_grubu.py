class MuzikGrubu:
    grup_ad = None
    gitarist1 = None
    gitarist2 = None
    davulcu = None

    def acilis(self):
        print(self.grup_ad + " konserine Hoşgeldiniz")
        print(self.gitarist1.gitar_turu + " -> " + self.gitarist1.ad)
        print(self.gitarist1.gitar_turu + " -> " + self.gitarist2.ad)
        print(" Davul -> " + self.davulcu.ad)
