class Gitarist:
    ad = None
    gitar_turu = None

    def nota_cal(self, nota_ad, tekrar_sayisi):
        for i in range(tekrar_sayisi):
            print(self.gitar_turu + " -> "+nota_ad)
