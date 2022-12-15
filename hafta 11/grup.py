class Grup:
    def __init__(self, grup_ad, mac_liste) -> None:
        self.grup_ad = grup_ad
        self.mac_liste = mac_liste

    def en_fazla_gol_atilan_mac(self):
        mac_adi = ""
        mac_skor = 0
        for mac in self.mac_liste:
            skor = mac.skor
            skor_list = skor.split("-")
            skor_toplam = int(skor_list[0])+int(skor_list[1])
            if skor_toplam > mac_skor:
                mac_skor = skor_toplam
                mac_adi = mac.takim1.takim_ad+"-"+mac.takim2.takim_ad

        print(mac_adi)

    def ilk_mac_bilgileri_yazdir(self):
        tarihler = []
        for mac in self.mac_liste:
            tarihler.append(mac.tarih)

        tarihler.sort()
        ilk_mac_tarihi = tarihler[0]
        for mac in self.mac_liste:
            if (mac.tarih == ilk_mac_tarihi):
                print(mac.takim1.takim_ad+"-"+mac.takim2.takim_ad)
                break

    def takim_istatistikler(self, takimlar):
        for takim in takimlar:
            for mac in self.mac_liste:
                skor = mac.skor
                skorlar = skor.split("-")
                if mac.takim1 == takim:
                    takim.atilan_gol = takim.atilan_gol+int(skorlar[0])
                    takim.yenilen_gol = takim.yenilen_gol+int(skorlar[1])
                    if int(skorlar[0] > skorlar[1]):
                        takim.puan = takim.puan+3
                    elif int(skorlar[0] == skorlar[1]):
                        takim.puan = takim.puan+1
                elif mac.takim2 == takim:
                    takim.atilan_gol = takim.atilan_gol+int(skorlar[1])
                    takim.yenilen_gol = takim.yenilen_gol+int(skorlar[0])
                    if int(skorlar[0] < skorlar[1]):
                        takim.puan = takim.puan+3
                    elif int(skorlar[0] == skorlar[1]):
                        takim.puan = takim.puan+1
        return takimlar

    def birinci_takim(self, takimlar):
        takim_istatistik = self.takim_istatistikler(takimlar)
        en_yuksek_puan = 0
        en_yuksek_puanli_takim = ""
        for takim in takim_istatistik:
            if takim.puan > en_yuksek_puan:
                en_yuksek_puan = takim.puan
                en_yuksek_puanli_takim = takim.takim_ad

        print(en_yuksek_puanli_takim+" - Puanı: "+str(en_yuksek_puan))

    def sonuncu_takim(self, takimlar):
        takim_istatistik = self.takim_istatistikler(takimlar)
        en_dusuk_puan = 100
        en_dusuk_puanli_takim = ""
        for takim in takim_istatistik:
            if takim.puan < en_dusuk_puan:
                en_dusuk_puan = takim.puan
                en_dusuk_puanli_takim = takim.takim_ad

        print(en_dusuk_puanli_takim+" - Puanı: "+str(en_dusuk_puan))
