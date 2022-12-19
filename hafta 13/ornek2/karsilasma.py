class Karsilasma:
    def __init__(self, takim_listesi):
        self.takim_listesi = takim_listesi

    def savas_basla(self):
        i = 0
        while self.takim_listesi[0].can > 0 and self.takim_listesi[1].can > 0:
            i += 1
            print("Tur : {}".format(str(i)))
            self.takim_listesi[0].karakter_listesi.sort(
                key=lambda x: x.karakter_tip.oncelik, reverse=True)
            self.takim_listesi[1].karakter_listesi.sort(
                key=lambda x: x.karakter_tip.oncelik, reverse=True)

            for karakter in self.takim_listesi[0].karakter_listesi:
                self.takim_listesi[1].can -= karakter.karakter_tip.vurus_guc

            if self.takim_listesi[1].can > 0:
                for karakter in self.takim_listesi[1].karakter_listesi:
                    self.takim_listesi[0].can -= karakter.karakter_tip.vurus_guc

        print("Kazanan Takım Üyeleri")
        if self.takim_listesi[0].can > 0:
            for karakter in self.takim_listesi[0].karakter_listesi:
                print(karakter.karakter_ad)
        else:
            for karakter in self.takim_listesi[1].karakter_listesi:
                print(karakter.karakter_ad)
