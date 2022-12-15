from grup import Grup
from takim import Takim
from mac import Mac

takim1 = Takim("Brezilya")
takim2 = Takim("Almanya")
takim3 = Takim("İspanya")
takim4 = Takim("Arjantin")

mac1 = Mac(takim1, takim2, "05-12-2022", "1-0")
mac2 = Mac(takim1, takim3, "06-12-2022", "1-1")
mac3 = Mac(takim1, takim4, "07-12-2022", "1-3")
mac4 = Mac(takim2, takim1, "08-12-2022", "1-3")
mac5 = Mac(takim2, takim3, "09-12-2022", "1-1")
mac6 = Mac(takim2, takim4, "10-12-2022", "0-0")
mac7 = Mac(takim3, takim1, "11-12-2022", "0-1")
mac8 = Mac(takim3, takim2, "12-12-2022", "0-3")
mac9 = Mac(takim3, takim4, "13-12-2022", "2-0")
mac10 = Mac(takim4, takim1, "14-12-2022", "2-2")
mac11 = Mac(takim4, takim2, "15-12-2022", "3-4")
mac12 = Mac(takim4, takim3, "16-12-2022", "1-3")

grup = Grup("Milli Takımlar",
            [mac1, mac2, mac3, mac4, mac5, mac6, mac7, mac8, mac9, mac10, mac11, mac12])

grup.en_fazla_gol_atilan_mac()
grup.ilk_mac_bilgileri_yazdir()
#grup.birinci_takim([takim1, takim2, takim3, takim4])
grup.sonuncu_takim([takim1, takim2, takim3, takim4])
