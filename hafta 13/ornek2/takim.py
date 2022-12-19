class Takim:
    def __init__(self, karakter_listesi):
        self.karakter_listesi = karakter_listesi
        self.can = 0
        for karakter in karakter_listesi:
            self.can += karakter.karakter_tip.can
